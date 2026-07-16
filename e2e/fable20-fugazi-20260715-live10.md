# E2E Evidence — FABLE20-FUGAZI-20260715-LIVE10

## Run
- **Run ID:** FABLE20-FUGAZI-20260715-LIVE10
- **Origin:** human-origin via Slack connector: Jonathon (#agentos-bots)
- **Agent:** Fugazi (AgentOS orchestration parent)
- **Job ID:** `orch-20260716-00f39293`
- **Submitted:** 2026-07-16T04:47:34.381881+00:00
- **Completed:** 2026-07-16T04:47:56.447258+00:00
- **Goal:** FABLE20-FUGAZI-20260715-LIVE10: 20 independent GPT-5.6 Sol Medium Hello World workers, each returning one NormalizedResult with a typed greeting/worker object, unique notes HELLO-WORLD-FUGAZI-NN, no tools or files.

## Routes / Auth / Fallback
- **Conductor:** anthropic/claude-fable-5 — auth `oauth`, credential authority `central_broker`
- **Worker:** codex/sdk — openai/gpt-5.6-sol — auth `oauth`, credential authority `central_broker`, reasoning effort `medium`
- **allow_api_key_fallback:** false
- **allow_failover:** false
- **fallback_used:** false
- **OAuth slot usage (codex pool, class `chatgpt-oauth`):** chatgpt-oauth-1 ×7, chatgpt-oauth-2 ×7, chatgpt-oauth-3 ×6

## JSONL Integrity
- **Source:** `/opt/data/orchestration/runs/orch-20260716-00f39293.jsonl`
- **Total events:** 62 — corrupt lines: 0
- **Event counts:** job_submitted 1, leg_queued 20, leg_started 20, leg_completed 20, job_completed 1
- **Forbidden events (salvage/retry/failure/error/timeout):** none
- **Legs:** 20/20 done — all served_by=primary, attempts=1, effort=medium (selected)
- **Typed results:** result_schema_valid 20/20, result_match 20/20, result_sha256 == expected_result_sha256 20/20, turn_evidence_sha256 == expected hash 20/20 (64-hex)
- **Criteria:** each leg 1 passed / 0 failed / 0 skipped with id `hello-NN`
- **Notes:** 20 unique — `Hello World | HELLO-WORLD-FUGAZI-01` … `-20`
- **Independent verification:** sha256 of each compact expected result `{"greeting":"Hello World","worker":"NN"}` recomputed and matched the recorded hashes

## Legs (full result / lineage)
| Leg | Result | Served by | Attempts | Effort | Engine/Surface | Provider/Model | Auth | Cred authority | Slot | Criteria | Schema valid | Result match | result_sha256 | turn_evidence_sha256 | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | `{"greeting":"Hello World","worker":"01"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | Hello World | HELLO-WORLD-FUGAZI-01 |
| hello-02 | `{"greeting":"Hello World","worker":"02"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | Hello World | HELLO-WORLD-FUGAZI-02 |
| hello-03 | `{"greeting":"Hello World","worker":"03"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | Hello World | HELLO-WORLD-FUGAZI-03 |
| hello-04 | `{"greeting":"Hello World","worker":"04"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | Hello World | HELLO-WORLD-FUGAZI-04 |
| hello-05 | `{"greeting":"Hello World","worker":"05"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | Hello World | HELLO-WORLD-FUGAZI-05 |
| hello-06 | `{"greeting":"Hello World","worker":"06"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | Hello World | HELLO-WORLD-FUGAZI-06 |
| hello-07 | `{"greeting":"Hello World","worker":"07"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | Hello World | HELLO-WORLD-FUGAZI-07 |
| hello-08 | `{"greeting":"Hello World","worker":"08"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | Hello World | HELLO-WORLD-FUGAZI-08 |
| hello-09 | `{"greeting":"Hello World","worker":"09"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | Hello World | HELLO-WORLD-FUGAZI-09 |
| hello-10 | `{"greeting":"Hello World","worker":"10"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | Hello World | HELLO-WORLD-FUGAZI-10 |
| hello-11 | `{"greeting":"Hello World","worker":"11"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | Hello World | HELLO-WORLD-FUGAZI-11 |
| hello-12 | `{"greeting":"Hello World","worker":"12"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | Hello World | HELLO-WORLD-FUGAZI-12 |
| hello-13 | `{"greeting":"Hello World","worker":"13"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | Hello World | HELLO-WORLD-FUGAZI-13 |
| hello-14 | `{"greeting":"Hello World","worker":"14"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | Hello World | HELLO-WORLD-FUGAZI-14 |
| hello-15 | `{"greeting":"Hello World","worker":"15"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | Hello World | HELLO-WORLD-FUGAZI-15 |
| hello-16 | `{"greeting":"Hello World","worker":"16"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | Hello World | HELLO-WORLD-FUGAZI-16 |
| hello-17 | `{"greeting":"Hello World","worker":"17"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | Hello World | HELLO-WORLD-FUGAZI-17 |
| hello-18 | `{"greeting":"Hello World","worker":"18"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | Hello World | HELLO-WORLD-FUGAZI-18 |
| hello-19 | `{"greeting":"Hello World","worker":"19"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | Hello World | HELLO-WORLD-FUGAZI-19 |
| hello-20 | `{"greeting":"Hello World","worker":"20"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | Hello World | HELLO-WORLD-FUGAZI-20 |

_Generated from the run JSONL by Fugazi. Full 64-hex digests available in the source JSONL._
