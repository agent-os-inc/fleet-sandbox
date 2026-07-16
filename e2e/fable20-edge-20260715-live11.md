# FABLE20-EDGE-20260715-LIVE11 — Production Acceptance Test

## Run

| Field | Value |
|---|---|
| Run | `FABLE20-EDGE-20260715-LIVE11` |
| Bot-origin driver | `forge` |
| Channel | `#agentos-bots` |
| Agent | Edge (`edge`) |
| Job ID | `orch-20260716-c8040e74` |
| Submitted (UTC) | `2026-07-16T04:17:47.829700+00:00` |
| Completed (UTC) | `2026-07-16T04:18:06.043385+00:00` |
| Goal | FABLE20-EDGE-20260715-LIVE11: 20-worker Hello World production acceptance test (bot-origin driver: forge). Each worker returns one NormalizedResult with an exact typed result. |

## Routes / Auth / Fallback

| Role | Engine/Surface | Provider/Model | Auth | Credential authority | Effort |
|---|---|---|---|---|---|
| Conductor | claude/sdk | anthropic/claude-fable-5 | oauth | central_broker | — |
| Worker | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | medium |

- `allow_api_key_fallback`: **false**
- `allow_failover`: **false**
- `fallback_used`: **false**
- Worker OAuth slot class: `chatgpt-oauth` (slots `chatgpt-oauth-1`, `chatgpt-oauth-2`, `chatgpt-oauth-3`; credential authority `central_broker`; no secrets recorded)

## JSONL Event Audit

- Source: `/opt/data/orchestration/runs/orch-20260716-c8040e74.jsonl`
- Total events: **62**, corrupt lines: **0**
- Counts: `job_submitted`=1, `leg_queued`=20, `leg_started`=20, `leg_completed`=20, `job_completed`=1
- Forbidden events (retry/salvage/failover/fallback/error/timeout/failure): **none**

## Results — 20/20 exact typed-result match

All 20 legs terminal `done` (per `leg_completed` events and terminal `orchestrate_status`): served_by `primary`, 1 attempt, selected effort `medium`, `result_schema_valid=true`, all criteria passed (1 passed / 0 failed / 0 skipped), `result_match=true`, and `result_sha256 == expected_result_sha256 == turn_evidence_sha256` (64-hex).

| Leg | State | Served by | Attempts | Effort | Criteria (P/F/S) | Schema valid | Match | result_sha256 = expected = turn_evidence | Lineage | Auth | Slot | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `hello-01` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-01`) | true | true | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-01` |
| `hello-02` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-02`) | true | true | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-02` |
| `hello-03` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-03`) | true | true | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-03` |
| `hello-04` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-04`) | true | true | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-04` |
| `hello-05` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-05`) | true | true | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-05` |
| `hello-06` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-06`) | true | true | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-06` |
| `hello-07` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-07`) | true | true | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-07` |
| `hello-08` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-08`) | true | true | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-08` |
| `hello-09` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-09`) | true | true | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-09` |
| `hello-10` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-10`) | true | true | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-10` |
| `hello-11` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-11`) | true | true | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-11` |
| `hello-12` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-12`) | true | true | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-12` |
| `hello-13` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-13`) | true | true | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-13` |
| `hello-14` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-14`) | true | true | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-14` |
| `hello-15` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-15`) | true | true | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-15` |
| `hello-16` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-16`) | true | true | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-16` |
| `hello-17` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-17`) | true | true | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-17` |
| `hello-18` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-18`) | true | true | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-2` | `Hello World | HELLO-WORLD-EDGE-18` |
| `hello-19` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-19`) | true | true | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-3` | `Hello World | HELLO-WORLD-EDGE-19` |
| `hello-20` | done | primary | 1 | medium (selected) | 1/0/0 (`hello-20`) | true | true | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` | codex/sdk · openai/gpt-5.6-sol | oauth (central_broker) | `chatgpt-oauth-1` | `Hello World | HELLO-WORLD-EDGE-20` |

## Verdict

**PASS** — 20/20 legs completed with exact typed-result match; single primary attempt each; OAuth-only routing with API-key fallback disabled and `fallback_used=false`.
