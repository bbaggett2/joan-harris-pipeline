/**
 * QDE blog schema (AEO) — built fresh on every page load from the published post.
 * WPCode: Code Type "PHP Snippet", Insertion "Auto Insert" > "Run Everywhere". Activate.
 * Owner: Cameron. Source of truth: GitHub cameron-tech-support/QDE_Blog_Schema_Snippet_v1.php
 *
 * Runs only on single blog posts that contain the QDE public FAQ section (<!-- qde-faq-start -->).
 * Outputs BlogPosting (with speakable -> #speakable-summary) + FAQPage, read from the live text,
 * so edits made in WordPress are reflected automatically. Also hides any old schema blocks
 * that were stored inside post content by earlier drafts, so nothing is duplicated.
 */

// 1) Remove old stored schema blocks from the visible content (they were saved by earlier drafts).
add_filter('the_content', function ($content) {
    if (strpos($content, 'qde-aeo-schema') === false) return $content;
    return preg_replace('#<script[^>]*qde-aeo-schema[^>]*>.*?</script>#s', '', $content);
}, 20);

// 2) Build and print the schema in <head>.
add_action('wp_head', function () {
    if (!is_singular('post')) return;
    $post = get_queried_object();
    if (!$post || $post->post_status !== 'publish') return;
    $raw = $post->post_content;
    if (strpos($raw, 'qde-faq-start') === false) return; // only QDE case articles

    $url   = get_permalink($post);
    $title = wp_strip_all_tags(get_the_title($post));
    $desc  = get_post_meta($post->ID, '_yoast_wpseo_metadesc', true);
    if (!$desc) $desc = wp_strip_all_tags(get_the_excerpt($post));
    $img   = get_the_post_thumbnail_url($post, 'full');

    $article = array(
        '@context' => 'https://schema.org',
        '@type' => 'BlogPosting',
        '@id' => trailingslashit($url) . '#article',
        'headline' => $title,
        'description' => $desc,
        'url' => $url,
        'mainEntityOfPage' => $url,
        'inLanguage' => 'en-US',
        'datePublished' => get_post_time('c', true, $post),
        'dateModified' => get_post_modified_time('c', true, $post),
        'author' => array(
            '@type' => 'Person',
            'name' => 'Bart Baggett',
            'jobTitle' => 'Forensic Handwriting Expert',
            'url' => 'https://bartbaggett.com',
            'knowsAbout' => array('handwriting', 'forensic document examination', 'expert testimony'),
        ),
        'publisher' => array(
            '@type' => 'Organization',
            'name' => 'Bart Baggett',
            'logo' => array('@type' => 'ImageObject', 'url' => 'https://bartbaggett.com/images/hsilogo2016.jpg'),
        ),
    );
    if ($img) $article['image'] = $img;
    if (strpos($raw, 'speakable-summary') !== false) {
        $article['speakable'] = array('@type' => 'SpeakableSpecification', 'cssSelector' => array('#speakable-summary'));
    }
    $graph = array($article);

    // FAQ: every <h3> question and the <p> answer after it, inside the public FAQ section.
    if (preg_match('#<!-- qde-faq-start -->(.*?)<!-- qde-faq-end -->#s', $raw, $m)) {
        preg_match_all('#<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>#s', $m[1], $qa, PREG_SET_ORDER);
        $items = array();
        foreach ($qa as $pair) {
            $q = trim(html_entity_decode(wp_strip_all_tags($pair[1]), ENT_QUOTES, 'UTF-8'));
            $a = trim(html_entity_decode(wp_strip_all_tags($pair[2]), ENT_QUOTES, 'UTF-8'));
            if ($q !== '' && $a !== '') {
                $items[] = array('@type' => 'Question', 'name' => $q,
                    'acceptedAnswer' => array('@type' => 'Answer', 'text' => $a));
            }
        }
        if ($items) {
            $graph[] = array('@context' => 'https://schema.org', '@type' => 'FAQPage',
                '@id' => trailingslashit($url) . '#faq', 'mainEntity' => $items);
        }
    }

    echo "\n<script type=\"application/ld+json\" id=\"qde-aeo-schema\">"
        . wp_json_encode($graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG)
        . "</script>\n";
}, 30);
