# E2E Acceptance Report — FABLE20-EDGE-20260715-LIVE6

- **Run nonce:** `FABLE20-EDGE-20260715-LIVE6`
- **Agent:** Edge (`edge`) — AgentOS orchestration parent
- **Bot-origin driver:** forge
- **Job ID:** `orch-20260716-1e8c0645`
- **Submitted:** 2026-07-16T02:49:19.210176+00:00
- **Completed:** 2026-07-16T02:49:38.800837+00:00
- **Conductor route:** anthropic / claude-fable-5 — auth: OAuth (credential_authority: central_broker)
- **Worker route:** codex / sdk — openai/gpt-5.6-sol — auth: OAuth (credential_authority: central_broker), reasoning effort: medium
- **API-key fallback:** disabled (`allow_api_key_fallback=false`); **failover:** disabled; **fallback_used:** false
- **Legs:** 20 submitted / 20 queued / 20 started / 20 completed — 20/20 done, 0 retries, 0 salvage, 0 failures/errors/timeouts
- **Journal:** 62 events, 0 corrupt lines (1 job_submitted + 20 leg_queued + 20 leg_started + 20 leg_completed + 1 job_completed)
- **Typed results:** 20/20 `result_schema_valid`, 20/20 `result_match` (result_sha256 == expected_result_sha256 == turn_evidence_sha256, 64-hex)
- **Criteria:** each leg 1 passed / 0 failed / 0 skipped (`hello-NN`)
- **OAuth worker slots used:** chatgpt-oauth-1, chatgpt-oauth-2, chatgpt-oauth-3

## Leg results and lineage (20/20)

| Leg | State | Result (typed) | Match | Schema | Criteria (pass/fail/skip) | Notes | Served by | Attempts | Effort | Engine/Surface | Provider/Model | Auth | Slot | Authority | result_sha256 = expected = turn_evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hello-01 | done | `{"greeting":"Hello World","worker":"01"}` | true | true | 1/0/0 (`hello-01`) | `Hello World | HELLO-WORLD-EDGE-01` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `03b6916af410d784509f87bfdd64aa957a90233b5a8e8fccd0b2b52854618aac` |
| hello-02 | done | `{"greeting":"Hello World","worker":"02"}` | true | true | 1/0/0 (`hello-02`) | `Hello World | HELLO-WORLD-EDGE-02` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `64e57950bf23a21363c12890b45d9be5d6d9f8530ad2fbcb68e661cd6fa94b33` |
| hello-03 | done | `{"greeting":"Hello World","worker":"03"}` | true | true | 1/0/0 (`hello-03`) | `Hello World | HELLO-WORLD-EDGE-03` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `a940a7f6dac35431b78079d16c83ca3b6c7f90a5138664d657b620d5c9036250` |
| hello-04 | done | `{"greeting":"Hello World","worker":"04"}` | true | true | 1/0/0 (`hello-04`) | `Hello World | HELLO-WORLD-EDGE-04` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `bff254d6ae6b665506e5ad7bbb857b3ba5f635a6e6c584d41f8e9b406ac2dc45` |
| hello-05 | done | `{"greeting":"Hello World","worker":"05"}` | true | true | 1/0/0 (`hello-05`) | `Hello World | HELLO-WORLD-EDGE-05` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `2ad151cec878b4aabb6c7fc8bca2b553929881f5fc2c6b2c9eef29d6d5484584` |
| hello-06 | done | `{"greeting":"Hello World","worker":"06"}` | true | true | 1/0/0 (`hello-06`) | `Hello World | HELLO-WORLD-EDGE-06` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `d3edfcabcda90e6ed889f9b2ba6a84f41f0248faaf75579302d06ccf238aae9a` |
| hello-07 | done | `{"greeting":"Hello World","worker":"07"}` | true | true | 1/0/0 (`hello-07`) | `Hello World | HELLO-WORLD-EDGE-07` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `900674101d16701089bad18ab1472e5cc7a36d793f30a6737630bc3db0b074c5` |
| hello-08 | done | `{"greeting":"Hello World","worker":"08"}` | true | true | 1/0/0 (`hello-08`) | `Hello World | HELLO-WORLD-EDGE-08` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `a6dd6431525bf04d21363d84bbf0a7eb80c46b5de041ed194ee4f74e5de91cf6` |
| hello-09 | done | `{"greeting":"Hello World","worker":"09"}` | true | true | 1/0/0 (`hello-09`) | `Hello World | HELLO-WORLD-EDGE-09` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `e4cdaec97b3d4c2a4aa3cd502abeba2878ee2a97e62d1e30e5fa21c532296f2c` |
| hello-10 | done | `{"greeting":"Hello World","worker":"10"}` | true | true | 1/0/0 (`hello-10`) | `Hello World | HELLO-WORLD-EDGE-10` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `32ee2a16c66df5ed3950b6ca23e48a0d6b121564b25d03f5eddb03868575791d` |
| hello-11 | done | `{"greeting":"Hello World","worker":"11"}` | true | true | 1/0/0 (`hello-11`) | `Hello World | HELLO-WORLD-EDGE-11` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `7b8632636d654e023f27aeac2f0cd665a2ce9f9b499d4cce11546ee43a5a5044` |
| hello-12 | done | `{"greeting":"Hello World","worker":"12"}` | true | true | 1/0/0 (`hello-12`) | `Hello World | HELLO-WORLD-EDGE-12` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `476ad98855e3185b9335e2ebc3623bf264458e36021fde7e4d6d0df09fc06b52` |
| hello-13 | done | `{"greeting":"Hello World","worker":"13"}` | true | true | 1/0/0 (`hello-13`) | `Hello World | HELLO-WORLD-EDGE-13` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `b17c6e2a664c31c39f84f34aa9eecadc0d1867ce5252c6abcfc00be9dd3902fe` |
| hello-14 | done | `{"greeting":"Hello World","worker":"14"}` | true | true | 1/0/0 (`hello-14`) | `Hello World | HELLO-WORLD-EDGE-14` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `1d36a1716a00e38a2b0b63398c1c3dee4e9c807149d8caa88ef5f7795ca6e64d` |
| hello-15 | done | `{"greeting":"Hello World","worker":"15"}` | true | true | 1/0/0 (`hello-15`) | `Hello World | HELLO-WORLD-EDGE-15` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `0a16fd15ded3af2cf627b03aa719e537a862c996c0746e2527bd8b2f285bc1e4` |
| hello-16 | done | `{"greeting":"Hello World","worker":"16"}` | true | true | 1/0/0 (`hello-16`) | `Hello World | HELLO-WORLD-EDGE-16` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `95ce8a2edbd98ecafdb48aa01f0366b32979c48d7e91886082e4d6258b2118d3` |
| hello-17 | done | `{"greeting":"Hello World","worker":"17"}` | true | true | 1/0/0 (`hello-17`) | `Hello World | HELLO-WORLD-EDGE-17` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `a79b1696d223bf172cc2436ea2a1f92ffa1bb5f4537685840785a29d5d6fdb67` |
| hello-18 | done | `{"greeting":"Hello World","worker":"18"}` | true | true | 1/0/0 (`hello-18`) | `Hello World | HELLO-WORLD-EDGE-18` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-2 | central_broker | `12a7d9167dc7d2a96fb3fdbc6cb815bc582d6a7747c19ddf95250c6b5e24db23` |
| hello-19 | done | `{"greeting":"Hello World","worker":"19"}` | true | true | 1/0/0 (`hello-19`) | `Hello World | HELLO-WORLD-EDGE-19` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-3 | central_broker | `1a9a2ff28ad6b9a517fababe2523512df96d4b2041664318c29f8ef613316bd3` |
| hello-20 | done | `{"greeting":"Hello World","worker":"20"}` | true | true | 1/0/0 (`hello-20`) | `Hello World | HELLO-WORLD-EDGE-20` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | chatgpt-oauth-1 | central_broker | `99eb4e77713507d52cfc34982fe1b5288072dc8472582a8d663b816ca5932ea0` |

Generated solely from `/opt/data/orchestration/runs/orch-20260716-1e8c0645.jsonl`.
