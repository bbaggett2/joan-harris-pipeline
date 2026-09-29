/**
 * Curt Baggett blog schema (AEO) for curtbaggett.com. Curt-only brand.
 * WPCode: Code Type "PHP Snippet", Insertion "Auto Insert" > "Run Everywhere". Activate.
 * Adapted from QDE_Blog_Schema_Snippet_v2.php. AIOSEO already prints the base graph
 * (BlogPosting, Person, Organization, WebPage), so this snippet does NOT print a second BlogPosting.
 *
 * 1) FAQPage: built from the post's "Frequently Asked Questions" H2 (question <p>, answer <p> pairs).
 * 2) Speakable: first FAQ answer gets id="speakable-summary" on the page.
 * 3) Enrichment of AIOSEO's BlogPosting: image (featured 'full'), speakable, description. (filter name to be verified on the live site)
 */

function cb_schema_faq_pairs($html) {
    $html = wpautop($html);
    if (!preg_match('#<h2[^>]*>\s*Frequently Asked Questions\s*</h2>(.*)$#is', $html, $m)) return array();
    $tail = preg_split('#<h[1-6][^>]*>#i', $m[1])[0];      // stop at the next heading
    preg_match_all('#<p[^>]*>(.*?)</p>#is', $tail, $ps);
    $out = array();
    $p = array_map(function ($x) { return trim(html_entity_decode(wp_strip_all_tags($x), ENT_QUOTES, 'UTF-8')); }, $ps[1]);
    $p = array_values(array_filter($p, function ($x) { return $x !== ''; }));
    for ($i = 0; $i + 1 < count($p); $i += 2) {
        if (substr($p[$i], -1) === '?') $out[] = array($p[$i], $p[$i + 1]);
    }
    return $out;
}

// 1) Mark the first FAQ answer as the speakable summary.
add_filter('the_content', function ($content) {
    if (!is_singular('post') || !in_the_loop() || !is_main_query()) return $content;
    if (strpos($content, 'speakable-summary') !== false) return $content;
    return preg_replace('#(<h2[^>]*>\s*Frequently Asked Questions\s*</h2>\s*<p[^>]*>.*?</p>\s*)<p>#is', '$1<p id="speakable-summary">', $content, 1);
}, 30);

// 2) FAQPage JSON-LD.
add_action('wp_head', function () {
    if (!is_singular('post')) return;
    $post = get_queried_object();
    if (!$post || $post->post_status !== 'publish') return;
    $pairs = cb_schema_faq_pairs($post->post_content);
    if (!$pairs) return;
    $url = get_permalink($post);
    $items = array();
    foreach ($pairs as $qa) {
        $items[] = array('@type' => 'Question', 'name' => $qa[0],
            'acceptedAnswer' => array('@type' => 'Answer', 'text' => $qa[1]));
    }
    $faq = array('@context' => 'https://schema.org', '@type' => 'FAQPage',
        '@id' => trailingslashit($url) . '#faq', 'isPartOf' => array('@id' => $url . '#webpage'),
        'mainEntity' => $items);
    echo "\n<script type=\"application/ld+json\" id=\"cb-faq-schema\">"
        . wp_json_encode($faq, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG)
        . "</script>\n";
}, 30);

// 3) Enrich AIOSEO's own BlogPosting (no second copy printed).
add_filter('aioseo_schema_output', function ($graphs) {
    if (!is_singular('post') || !is_array($graphs)) return $graphs;
    $post = get_queried_object();
    $img = get_the_post_thumbnail_url($post, 'full');
    foreach ($graphs as &$g) {
        if (isset($g['@type']) && $g['@type'] === 'BlogPosting') {
            if ($img && empty($g['image'])) $g['image'] = array('@type' => 'ImageObject', 'url' => $img, 'width' => 1200, 'height' => 675);
            $g['speakable'] = array('@type' => 'SpeakableSpecification', 'cssSelector' => array('#speakable-summary'));
            $g['about'] = array('@type' => 'Thing', 'name' => 'Forensic document examination');
        }
    }
    return $graphs;
}, 20);
