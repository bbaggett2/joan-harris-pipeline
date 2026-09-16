# 09 — YouTube (private upload, thumbnail, captions)
**V1 · 2026-09-15 · Governs n8n nodes: `Drive: download long` · `YouTube: upload` · `Wait for processing` · `YouTube: thumbnail` · `YouTube: captions`**

Replaces `yutu` + rclone + YouTube Studio. Google OAuth credential in n8n with scopes `youtube.upload youtube.force-ssl`.

## Order is fixed
1. **`Drive: download long`** — binary of the long cut (or the vertical if `VERTICAL_ONLY`).
2. **`YouTube: upload`** — YouTube node, *Video → Upload*: title = row `title`, description = row `description` (verbatim; preflight has already stripped markdown), category 27 (Education), `privacyStatus: private`, `selfDeclaredMadeForKids: false`, channel `UCrpyI5SkE075HJaFyxO_ozQ`. Store `youtube_id`.
   ⛔ Never Unlisted, Public or Scheduled. Never the HU channel. Never `UCbDGkQdUKEgeDTDvqVEWoWA`.
3. **Wait** ~90 s (v1), then `videos.list?part=processingDetails` loop until `succeeded` (build item).
4. **`YouTube: thumbnail`** — HTTP `POST https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId=` with the PNG binary from file 07 (`image/png`). *(v1 bug #1: the PNG binary must be re-attached with a Merge node before this call.)*
5. **`YouTube: captions`** — HTTP multipart `POST https://www.googleapis.com/upload/youtube/v3/captions?part=snippet` with `snippet: {videoId, language: "en", name: "English", isDraft: false}` + the VTT binary. Then `captions.list` and assert `trackKind = standard`. *(v1 bug #2: same re-attach.)*
   ⛔ Captions are the last YouTube step. Never before the thumbnail.
6. Playlist: `playlistItems.insert` into `yt_playlist_id` when configured; otherwise `notes` gets `NO_PLAYLIST`.

**Betty never changes visibility.** The reviewer making it public is the approval.

## Refinement hook
Upload metadata (category, tags, language) → here. Copy → files 04/05. Caption quality → file 03.
