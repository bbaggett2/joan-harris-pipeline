// Betty — QDE Daily Social Post v4 · "Preflight checks" Code node (LIVE 2026-09-12)
// Mode: Run Once for All Items. Input: the one READY row from "Queue has a post?".
// Preflight REPAIRS or FLAGS. It never blocks. Only an empty caption skips the row.
// Output keeps v3 field names: preflight_ok (false only when caption empty), preflight_problems (flag list).
// caption goes out CLEAN — flags live in the sheet `notes` column and the Slack message, never in the post.
const row = { ...$input.first().json };
const flags = [];
let cap = String(row.caption || '').trim();
// Repair Mac-Roman mojibake from the seed CSV import (‚Äî = —, ¬∑ = ·, etc.)
const MOJI = [['‚Äî','—'],['‚Äì','–'],['¬∑','·'],['‚Äô','’'],['‚Äò','‘'],['‚Äú','“'],['‚Äù','”'],['‚Ä¶','…'],['‚úÖ','✅'],['‚ö†Ô∏è','⚠️'],['¬Ω','½'],['√©','é']];
const demoji = s => MOJI.reduce((t,[a,b]) => t.split(a).join(b), String(s || ''));
cap = demoji(cap);
for (const k of ['headline','subline','torn_note','gold_word','fact_status','image_prompt','face_source']) row[k] = demoji(row[k]);
const PHONE = '1-800-980-9030';
const DOMAIN_OK = 'HandwritingExpertUSA.com';
const CTA = '\n\n' + PHONE + '\n' + DOMAIN_OK + ' · bartbaggett.com';

if (!cap) {
  return [{ json: { ...row, preflight_ok: false, preflight_problems: 'EMPTY CAPTION', flags: ['EMPTY CAPTION'] } }];
}

// --- repairs (mechanical only) ---
if (/HandwritingExpert\.com/i.test(cap)) { cap = cap.replace(/HandwritingExpert\.com/gi, DOMAIN_OK); flags.push('DOMAIN REPAIRED'); }
if (!cap.includes(PHONE) || !cap.includes(DOMAIN_OK)) { cap = cap + CTA; flags.push('CTA APPENDED'); }
const pointer = /[^.!?\n]*\b(link in (my )?bio|full (breakdown|video|episode) on (youtube|tiktok|instagram)|watch (the )?full (video|episode))\b[^.!?\n]*[.!?]?/gi;
if (pointer.test(cap)) { cap = cap.replace(pointer, '').replace(/\n{3,}/g, '\n\n'); flags.push('POINTER REMOVED'); }

// --- flags (reviewer fixes in the sheet / Metricool) ---
if (/graphol/i.test(cap.replace(/#\w+/g, ''))) flags.push('BANNED TERM');
if (/\[TO VERIFY\]|\*\*\*\*/.test(cap)) flags.push('TO VERIFY IN COPY');
if (/win your case|guarantee/i.test(cap)) flags.push('OUTCOME LANGUAGE');
if (String(row.facts_need_verify || '').toUpperCase() === 'YES') flags.push('FACTS UNVERIFIED');
const facePending = String(row.photo_required || '').toUpperCase() === 'YES' && !String(row.image_url || '').trim();
if (facePending) flags.push('FACE PENDING');

return [{ json: {
  ...row,
  caption: cap,
  caption_clean: cap,
  flags,
  face_pending: facePending,
  preflight_ok: true,
  preflight_problems: flags.length ? flags.join('; ') : 'none',
} }];
