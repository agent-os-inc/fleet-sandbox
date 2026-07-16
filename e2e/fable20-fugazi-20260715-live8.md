# E2E Run Report: FABLE20-FUGAZI-20260715-LIVE8

## Run / Agent / Job

| Field | Value |
|---|---|
| Run ID | FABLE20-FUGAZI-20260715-LIVE8 |
| Agent | Fugazi (AgentOS orchestration parent) |
| Bot-origin driver | forge |
| Job ID | orch-20260716-712d84b9 |
| Goal | FABLE20-FUGAZI-20260715-LIVE8: 20 independent GPT-5.6 Sol Medium worker legs each returning a typed Hello World result with worker-specific NN, exact schema/expected-result match, no tools/files. |
| Submitted at | 2026-07-16T03:15:30.661477+00:00 |
| Completed at | 2026-07-16T03:15:55.057057+00:00 |
| Legs submitted | 20 |
| Event counts | 1 submitted / 20 queued / 20 started / 20 completed / 1 job completed |
| Corrupt JSONL lines | 0 |

## Routes / Auth / Fallback

| Field | Value |
|---|---|
| Conductor | anthropic/claude-fable-5 |
| Conductor auth | oauth (credential_authority=central_broker) |
| Worker route | codex/sdk → openai/gpt-5.6-sol |
| Worker auth | oauth (credential_authority=central_broker) |
| Worker reasoning effort | medium |
| API-key fallback allowed | False |
| Failover allowed | False |
| fallback_used | False |
| Worker OAuth slots used | chatgpt-oauth-1 (7 legs), chatgpt-oauth-2 (7 legs), chatgpt-oauth-3 (6 legs) |

## Leg Results (20/20 done, exact typed-result match)

Every leg: served_by=primary, attempts=1, effort=medium (selected), result_schema_valid=true, all criteria passed (1 passed / 0 failed / 0 skipped), result_match=true, result_sha256 = expected_result_sha256 = turn_evidence_sha256.

| Leg | Criteria ID | Pass | Match | Result SHA-256 (= expected = turn evidence) | Engine/Surface | Provider/Model | Auth | Slot | Notes | Tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | hello-01 | 1/1 | true | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-01 | 13902/62 |
| hello-02 | hello-02 | 1/1 | true | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-02 | 13788/62 |
| hello-03 | hello-03 | 1/1 | true | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-03 | 13870/62 |
| hello-04 | hello-04 | 1/1 | true | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-04 | 13865/62 |
| hello-05 | hello-05 | 1/1 | true | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-05 | 13892/62 |
| hello-06 | hello-06 | 1/1 | true | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-06 | 13798/62 |
| hello-07 | hello-07 | 1/1 | true | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-07 | 13860/62 |
| hello-08 | hello-08 | 1/1 | true | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-08 | 13798/62 |
| hello-09 | hello-09 | 1/1 | true | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-09 | 13783/62 |
| hello-10 | hello-10 | 1/1 | true | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-10 | 13865/62 |
| hello-11 | hello-11 | 1/1 | true | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-11 | 13892/62 |
| hello-12 | hello-12 | 1/1 | true | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-12 | 13860/62 |
| hello-13 | hello-13 | 1/1 | true | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-13 | 13798/62 |
| hello-14 | hello-14 | 1/1 | true | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-14 | 13892/62 |
| hello-15 | hello-15 | 1/1 | true | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-15 | 13798/62 |
| hello-16 | hello-16 | 1/1 | true | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-16 | 13880/62 |
| hello-17 | hello-17 | 1/1 | true | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-17 | 13897/62 |
| hello-18 | hello-18 | 1/1 | true | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | Hello World \| HELLO-WORLD-FUGAZI-18 | 13793/62 |
| hello-19 | hello-19 | 1/1 | true | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | Hello World \| HELLO-WORLD-FUGAZI-19 | 13865/62 |
| hello-20 | hello-20 | 1/1 | true | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | Hello World \| HELLO-WORLD-FUGAZI-20 | 13892/62 |

## Verdict

PASS — 20/20 legs done with exact typed-result match, unique notes HELLO-WORLD-FUGAZI-01..-20, no salvage/retry/failure/error/timeout events, fallback_used=false.
