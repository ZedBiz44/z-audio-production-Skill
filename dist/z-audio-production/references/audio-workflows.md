# Audio Production Workflows

## Script Lock And Proof Rules

- Record the script version, approval owner, pronunciation guide, intended runtime, and speaker before production.
- Expand or annotate acronyms, numbers, URLs, dates, and difficult names when the engine needs phonetic help.
- Read the script aloud or generate a cheap proof to test runtime and phrasing.
- A proof may use a temporary voice. Label it clearly and never pass it downstream as the approved master.
- Any wording change creates a new script version and reopens audio approval for the affected passage.

## Voice Audition Or Clone Creation

- Use clean, single-speaker source audio without music, reverb, background speech, or aggressive processing.
- Follow the selected provider's current sample-length and format requirements rather than relying on old notes.
- Confirm consent and permitted uses before upload.
- Create short same-script auditions and review them at normal playback speed on headphones and ordinary speakers.
- Save the chosen identity, settings, audition file, and approval decision in the Voice Identity Package.

## Master Narration

- Generate the complete dry narration when the provider supports reliable long-form output.
- For engines with length limits, generate planned sections using locked voice settings, then assemble them without altering wording.
- Maintain consistent silence, room tone, level, tone, and pacing across sections.
- Check the beginning and end for clipped consonants, missing words, truncated tails, or extra fabricated speech.
- Save the authoritative video-production master as 48 kHz PCM WAV unless the receiver requires another lossless format.
- Create MP3, AAC, or other compressed files only as review or delivery derivatives.

## Cleanup And Mastering

Apply only the processing the source needs:

- remove obvious clicks, excessive noise, and unintended long silences;
- use de-essing, EQ, compression, and noise reduction conservatively;
- keep a clean, unprocessed or minimally processed archive when substantial repair is required;
- avoid music, ambience, or sound effects in the dry master;
- prevent clipping and preserve natural breaths unless the brief requests a different style;
- measure loudness and true peak when delivery specifications require them.

When no delivery loudness is specified, report the measured level rather than applying an arbitrary platform master. The video assembly process may set final program loudness after music and effects are mixed.

## Scene-Safe Derivatives

- Create each scene file from the approved master at recorded start and end timecodes.
- Cut at silence, breaths, or natural phrase boundaries.
- Add handles only when the downstream editor requests them, and record their duration.
- Do not use time stretching to force narration into a visual slot without opening a new approval cycle.
- Do not regenerate a line simply because the avatar pose or visual scene changes.
- Keep a mapping from scene ID to master timecodes, derivative filename, text, and downstream consumer.

## Revision Control

- Correct the smallest failed passage.
- Reassemble a new master version and re-run listening and technical QC.
- Preserve the previous approved version until the replacement is approved.
- Regenerate only derivatives that depend on the changed passage.
- Record why the revision occurred, who approved it, and which downstream assets are now stale.
