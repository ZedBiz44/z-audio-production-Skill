# Audio-To-Video Handoff Contract

Use this contract whenever the future `z-video-production` skill or another video workflow consumes audio.

## Audio Skill Responsibilities

The audio skill provides:

- approved lossless dry master, normally 48 kHz PCM WAV;
- final script and script version;
- speaker and pronunciation record;
- duration and technical inspection result;
- optional exact scene extracts with master timecodes;
- optional transcript, word timing, or caption-timing source data;
- Voice Identity Package reference;
- audio manifest, provider job IDs, costs, approvals, and QC status.

## Video Skill Responsibilities

The video skill owns:

- avatar and lip-sync video generation;
- visual identity and character reference packages;
- scene plans, B-roll, stock footage, and image generation;
- visible captions, graphics, logos, and typography;
- Remotion or other edit timelines, compositing, mixing, proofs, and final video exports.

## Shared Invariants

- The approved full master remains the authoritative soundtrack.
- Lip-sync and avatar tools receive exact extracts from that master.
- If a provider returns video with embedded audio, the video workflow aligns the visuals to the authoritative master and normally mutes the returned duplicate audio.
- Music and sound effects remain separate until the video mix.
- A visual revision must not trigger audio regeneration unless the script or approved performance changes.
- An audio revision marks affected avatar clips, timing files, captions, and video proofs as stale.
- The video skill may request a new audio version, but it must not silently edit or replace the approved master.

## Minimum Handoff Manifest Fields

- project ID and project name;
- audio package version and approval status;
- master filename, duration, sample rate, channels, and hash when required;
- script version and language;
- speaker, voice provider, model, and private voice reference by secure identifier;
- scene IDs, timecodes, derivative filenames, and exact text;
- transcript or timing filename;
- known pronunciation decisions and open issues;
- cost and provider job references;
- downstream owner and handoff date.

## Acceptance Check

The video workflow should reject the handoff when the master is unapproved, the script versions disagree, required files are missing, scene timecodes exceed the master duration, or consent and voice identity references are unresolved.
