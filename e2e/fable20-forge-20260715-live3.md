# E2E Evidence — FABLE20-FORGE-20260715-LIVE3

- **Run ID:** `FABLE20-FORGE-20260715-LIVE3`
- **Agent:** forge (Forge)
- **Job ID:** `orch-20260716-13cb7672`
- **Job state:** completed (2026-07-16T02:10:14.438302+00:00 → 2026-07-16T02:10:35.448078+00:00 UTC)
- **Source of truth:** `/opt/data/orchestration/runs/orch-20260716-13cb7672.jsonl` (62 lines, 0 corrupt)

## Routing

| Role | Engine | Surface | Provider/Model | Auth mode | Credential authority |
|---|---|---|---|---|---|
| Conductor | claude | sdk | anthropic/claude-fable-5 | oauth | central_broker |
| Worker | codex | sdk | openai/gpt-5.6-sol | oauth | central_broker |

- **Worker reasoning effort:** medium (effort_source=selected on all legs)
- **Fallback policy:** allow_api_key_fallback=false, allow_failover=false, fallback_used=false
- **Worker credential slot class:** codex pool (`chatgpt-oauth-1|2|3`), brokered by central_broker
- **Image digest:** not available

## Event ledger summary

- job_submitted: 1 (legs=20)
- leg_queued: 20 unique (hello-01..hello-20)
- leg_started: 20 unique (hello-01..hello-20)
- leg_completed: 20 unique (hello-01..hello-20)
- job_completed: 1
- salvage/retry/failure/error/timeout events: 0
- turn_evidence_sha256 == expected_result_sha256 on all 20 legs; expected hash independently re-derived from canonical compact JSON on 20/20 legs

## Legs

| Leg | State | Served by | Attempts | Effort | Criteria | Schema valid | All pass | Result match | Result SHA-256 | Engine | Surface | Provider | Model | Auth | Cred authority | Credential | Turn evidence SHA-256 | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-01) | true | true | true | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | Hello World | HELLO-WORLD-FORGE-01 |
| hello-02 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-02) | true | true | true | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | Hello World | HELLO-WORLD-FORGE-02 |
| hello-03 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-03) | true | true | true | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | Hello World | HELLO-WORLD-FORGE-03 |
| hello-04 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-04) | true | true | true | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | Hello World | HELLO-WORLD-FORGE-04 |
| hello-05 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-05) | true | true | true | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | Hello World | HELLO-WORLD-FORGE-05 |
| hello-06 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-06) | true | true | true | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | Hello World | HELLO-WORLD-FORGE-06 |
| hello-07 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-07) | true | true | true | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | Hello World | HELLO-WORLD-FORGE-07 |
| hello-08 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-08) | true | true | true | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | Hello World | HELLO-WORLD-FORGE-08 |
| hello-09 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-09) | true | true | true | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | Hello World | HELLO-WORLD-FORGE-09 |
| hello-10 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-10) | true | true | true | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | Hello World | HELLO-WORLD-FORGE-10 |
| hello-11 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-11) | true | true | true | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | Hello World | HELLO-WORLD-FORGE-11 |
| hello-12 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-12) | true | true | true | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | Hello World | HELLO-WORLD-FORGE-12 |
| hello-13 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-13) | true | true | true | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | Hello World | HELLO-WORLD-FORGE-13 |
| hello-14 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-14) | true | true | true | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | Hello World | HELLO-WORLD-FORGE-14 |
| hello-15 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-15) | true | true | true | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | Hello World | HELLO-WORLD-FORGE-15 |
| hello-16 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-16) | true | true | true | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | Hello World | HELLO-WORLD-FORGE-16 |
| hello-17 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-17) | true | true | true | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | Hello World | HELLO-WORLD-FORGE-17 |
| hello-18 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-18) | true | true | true | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | Hello World | HELLO-WORLD-FORGE-18 |
| hello-19 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-19) | true | true | true | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | Hello World | HELLO-WORLD-FORGE-19 |
| hello-20 | done | primary | 1 | medium | 1/1 pass, 0 fail, 0 skip (hello-20) | true | true | true | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | codex | sdk | openai | gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | Hello World | HELLO-WORLD-FORGE-20 |
