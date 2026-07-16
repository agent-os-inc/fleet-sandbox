# E2E Evidence: FABLE20-FORGE-20260715-LIVE13

Production acceptance test — Forge (Fable conductor) + 20 GPT-5.6 Sol Medium Hello World workers.

## Run

| Field | Value |
|---|---|
| Run ID | FABLE20-FORGE-20260715-LIVE13 |
| Agent | forge (Forge) |
| Bot-origin driver | edge |
| Job ID | orch-20260716-ccdf5006 |
| Submitted | 2026-07-16T04:32:39.519690+00:00 |
| Completed | 2026-07-16T04:32:58.765380+00:00 |
| Legs | 20 submitted / 20 done |
| Conductor route | anthropic/claude-fable-5 (auth: oauth, authority: central_broker) |
| Worker route | codex/sdk openai/gpt-5.6-sol (auth: oauth, authority: central_broker, effort: medium) |
| API-key fallback allowed | false |
| Fallback used | false |
| Credential slot class | chatgpt-oauth (central_broker); slots chatgpt-oauth-1/2/3 |

## Event ledger (from run JSONL)

| Event | Count |
|---|---|
| job_submitted | 1 |
| leg_queued | 20 |
| leg_started | 20 |
| leg_completed | 20 |
| job_completed | 1 |
| total | 62 |

0 corrupt lines. No salvage/retry/failure/error/timeout/fallback events.

## Legs (20/20 done)

| Leg | State | Served by | Attempts | Effort (src) | Slot | Lineage | Schema valid | All pass | Result match | Criteria P/F/S | result_sha256 = expected = turn_evidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | Hello World | HELLO-WORLD-FORGE-01 |
| hello-02 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | Hello World | HELLO-WORLD-FORGE-02 |
| hello-03 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | Hello World | HELLO-WORLD-FORGE-03 |
| hello-04 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | Hello World | HELLO-WORLD-FORGE-04 |
| hello-05 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | Hello World | HELLO-WORLD-FORGE-05 |
| hello-06 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | Hello World | HELLO-WORLD-FORGE-06 |
| hello-07 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | Hello World | HELLO-WORLD-FORGE-07 |
| hello-08 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | Hello World | HELLO-WORLD-FORGE-08 |
| hello-09 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | Hello World | HELLO-WORLD-FORGE-09 |
| hello-10 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | Hello World | HELLO-WORLD-FORGE-10 |
| hello-11 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | Hello World | HELLO-WORLD-FORGE-11 |
| hello-12 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | Hello World | HELLO-WORLD-FORGE-12 |
| hello-13 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | Hello World | HELLO-WORLD-FORGE-13 |
| hello-14 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | Hello World | HELLO-WORLD-FORGE-14 |
| hello-15 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | Hello World | HELLO-WORLD-FORGE-15 |
| hello-16 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | Hello World | HELLO-WORLD-FORGE-16 |
| hello-17 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | Hello World | HELLO-WORLD-FORGE-17 |
| hello-18 | done | primary | 1 | medium (selected) | chatgpt-oauth-1 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | Hello World | HELLO-WORLD-FORGE-18 |
| hello-19 | done | primary | 1 | medium (selected) | chatgpt-oauth-2 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | Hello World | HELLO-WORLD-FORGE-19 |
| hello-20 | done | primary | 1 | medium (selected) | chatgpt-oauth-3 | codex/sdk openai/gpt-5.6-sol (oauth, central_broker) | true | true | true | 1/0/0 | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | Hello World | HELLO-WORLD-FORGE-20 |

## Typed-result verification

Each leg returned exactly `{"greeting":"Hello World","worker":"NN"}` validated against the strict schema
(`additionalProperties=false`, required `greeting`+`worker`). For all 20 legs, `sha256(canonical expected JSON)`
was independently re-derived and equals `result_sha256`, `expected_result_sha256`, and `turn_evidence_sha256` (20/20 exact typed-result matches).
Criteria: each leg 1 passed, 0 failed, 0 skipped, id `hello-NN`. Notes unique: `Hello World | HELLO-WORLD-FORGE-01`..`-20`.

Source of truth: `/opt/data/orchestration/runs/orch-20260716-ccdf5006.jsonl` (62 events, 0 corrupt lines).

