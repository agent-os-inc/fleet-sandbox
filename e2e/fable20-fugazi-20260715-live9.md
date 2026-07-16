# FABLE20-FUGAZI-20260715-LIVE9 — Fugazi Fable + GPT-5.6 20-worker Hello World

## Run

| Field | Value |
|---|---|
| Run name | FABLE20-FUGAZI-20260715-LIVE9 |
| Bot-origin driver | forge |
| Channel | #all-agentos |
| Job ID | `orch-20260716-70e9f91f` |
| Submitted | 2026-07-16T03:46:54.652123+00:00 |
| Completed | 2026-07-16T03:47:15.439864+00:00 |
| Goal | FABLE20-FUGAZI-20260715-LIVE9: 20 independent GPT-5.6 Sol Medium worker legs each returning a typed Hello World NormalizedResult |

## Agent

| Field | Value |
|---|---|
| Agent | Fugazi (`fugazi`) |
| Orchestration | AgentOS parent conductor + 20 independent worker legs |

## Job / Event ledger

| Event | Count |
|---|---|
| job_submitted | 1 |
| leg_queued | 20 |
| leg_started | 20 |
| leg_completed | 20 |
| job_completed | 1 |
| **Total events** | **62** |
| Corrupt lines | 0 |

## Routes / Auth / Fallback

| Field | Value |
|---|---|
| Conductor | anthropic/claude-fable-5 (oauth, authority=central_broker) |
| Worker | codex/sdk — openai/gpt-5.6-sol (oauth, authority=central_broker, effort=medium) |
| Worker OAuth slots used | `chatgpt-oauth-1`, `chatgpt-oauth-2`, `chatgpt-oauth-3` |
| allow_api_key_fallback | false |
| allow_failover | false |
| fallback_used | false |

## Result summary

- Legs: **20/20 done** (primary, 1 attempt each, no salvage/retry)
- Typed results: **20/20 exact match** (`result_match=true`, `result_schema_valid=true`, `result_sha256 == expected_result_sha256` for every leg)
- Criteria: 20/20 legs with 1 passed, 0 failed, 0 skipped
- Notes nonces: `HELLO-WORLD-FUGAZI-01` .. `HELLO-WORLD-FUGAZI-20`, all unique

## Full result / lineage table

| Leg | State | Served by | Attempts | Effort (source) | Engine/Surface | Provider/Model | Auth | Authority | OAuth slot | Schema valid | All pass | Match | Criteria (P/F/S) | result_sha256 == expected & evidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `03b6916af410d784…` | Hello World | HELLO-WORLD-FUGAZI-01 |
| hello-02 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `64e57950bf23a213…` | Hello World | HELLO-WORLD-FUGAZI-02 |
| hello-03 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `a940a7f6dac35431…` | Hello World | HELLO-WORLD-FUGAZI-03 |
| hello-04 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `bff254d6ae6b6655…` | Hello World | HELLO-WORLD-FUGAZI-04 |
| hello-05 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `2ad151cec878b4aa…` | Hello World | HELLO-WORLD-FUGAZI-05 |
| hello-06 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `d3edfcabcda90e6e…` | Hello World | HELLO-WORLD-FUGAZI-06 |
| hello-07 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `900674101d167010…` | Hello World | HELLO-WORLD-FUGAZI-07 |
| hello-08 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `a6dd6431525bf04d…` | Hello World | HELLO-WORLD-FUGAZI-08 |
| hello-09 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `e4cdaec97b3d4c2a…` | Hello World | HELLO-WORLD-FUGAZI-09 |
| hello-10 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `32ee2a16c66df5ed…` | Hello World | HELLO-WORLD-FUGAZI-10 |
| hello-11 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `7b8632636d654e02…` | Hello World | HELLO-WORLD-FUGAZI-11 |
| hello-12 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `476ad98855e3185b…` | Hello World | HELLO-WORLD-FUGAZI-12 |
| hello-13 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `b17c6e2a664c31c3…` | Hello World | HELLO-WORLD-FUGAZI-13 |
| hello-14 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `1d36a1716a00e38a…` | Hello World | HELLO-WORLD-FUGAZI-14 |
| hello-15 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `0a16fd15ded3af2c…` | Hello World | HELLO-WORLD-FUGAZI-15 |
| hello-16 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `95ce8a2edbd98eca…` | Hello World | HELLO-WORLD-FUGAZI-16 |
| hello-17 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `a79b1696d223bf17…` | Hello World | HELLO-WORLD-FUGAZI-17 |
| hello-18 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-3` | true | true | true | 1/0/0 | yes — `12a7d9167dc7d2a9…` | Hello World | HELLO-WORLD-FUGAZI-18 |
| hello-19 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-2` | true | true | true | 1/0/0 | yes — `1a9a2ff28ad6b9a5…` | Hello World | HELLO-WORLD-FUGAZI-19 |
| hello-20 | done | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | `chatgpt-oauth-1` | true | true | true | 1/0/0 | yes — `99eb4e77713507d5…` | Hello World | HELLO-WORLD-FUGAZI-20 |

## Evidence hashes (sha256, full)

| Leg | result_sha256 = expected_result_sha256 = turn_evidence_sha256 |
|---|---|
| hello-01 | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` |
| hello-02 | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` |
| hello-03 | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` |
| hello-04 | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` |
| hello-05 | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` |
| hello-06 | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` |
| hello-07 | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` |
| hello-08 | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` |
| hello-09 | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` |
| hello-10 | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` |
| hello-11 | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` |
| hello-12 | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` |
| hello-13 | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` |
| hello-14 | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` |
| hello-15 | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` |
| hello-16 | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` |
| hello-17 | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` |
| hello-18 | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` |
| hello-19 | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` |
| hello-20 | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` |

_Generated solely from `/opt/data/orchestration/runs/orch-20260716-70e9f91f.jsonl` (62 events, 0 corrupt lines)._
