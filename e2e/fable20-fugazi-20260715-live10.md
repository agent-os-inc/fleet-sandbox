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
| hello-01 | `{"greeting":"Hello World","worker":"01"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `03b6916af410…` | `03b6916af410…` | Hello World | HELLO-WORLD-FUGAZI-01 |
| hello-02 | `{"greeting":"Hello World","worker":"02"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `64e57950bf23…` | `64e57950bf23…` | Hello World | HELLO-WORLD-FUGAZI-02 |
| hello-03 | `{"greeting":"Hello World","worker":"03"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `a940a7f6dac3…` | `a940a7f6dac3…` | Hello World | HELLO-WORLD-FUGAZI-03 |
| hello-04 | `{"greeting":"Hello World","worker":"04"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `bff254d6ae6b…` | `bff254d6ae6b…` | Hello World | HELLO-WORLD-FUGAZI-04 |
| hello-05 | `{"greeting":"Hello World","worker":"05"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `2ad151cec878…` | `2ad151cec878…` | Hello World | HELLO-WORLD-FUGAZI-05 |
| hello-06 | `{"greeting":"Hello World","worker":"06"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `d3edfcabcda9…` | `d3edfcabcda9…` | Hello World | HELLO-WORLD-FUGAZI-06 |
| hello-07 | `{"greeting":"Hello World","worker":"07"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `900674101d16…` | `900674101d16…` | Hello World | HELLO-WORLD-FUGAZI-07 |
| hello-08 | `{"greeting":"Hello World","worker":"08"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `a6dd6431525b…` | `a6dd6431525b…` | Hello World | HELLO-WORLD-FUGAZI-08 |
| hello-09 | `{"greeting":"Hello World","worker":"09"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `e4cdaec97b3d…` | `e4cdaec97b3d…` | Hello World | HELLO-WORLD-FUGAZI-09 |
| hello-10 | `{"greeting":"Hello World","worker":"10"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `32ee2a16c66d…` | `32ee2a16c66d…` | Hello World | HELLO-WORLD-FUGAZI-10 |
| hello-11 | `{"greeting":"Hello World","worker":"11"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `7b8632636d65…` | `7b8632636d65…` | Hello World | HELLO-WORLD-FUGAZI-11 |
| hello-12 | `{"greeting":"Hello World","worker":"12"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `476ad98855e3…` | `476ad98855e3…` | Hello World | HELLO-WORLD-FUGAZI-12 |
| hello-13 | `{"greeting":"Hello World","worker":"13"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `b17c6e2a664c…` | `b17c6e2a664c…` | Hello World | HELLO-WORLD-FUGAZI-13 |
| hello-14 | `{"greeting":"Hello World","worker":"14"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `1d36a1716a00…` | `1d36a1716a00…` | Hello World | HELLO-WORLD-FUGAZI-14 |
| hello-15 | `{"greeting":"Hello World","worker":"15"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `0a16fd15ded3…` | `0a16fd15ded3…` | Hello World | HELLO-WORLD-FUGAZI-15 |
| hello-16 | `{"greeting":"Hello World","worker":"16"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `95ce8a2edbd9…` | `95ce8a2edbd9…` | Hello World | HELLO-WORLD-FUGAZI-16 |
| hello-17 | `{"greeting":"Hello World","worker":"17"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `a79b1696d223…` | `a79b1696d223…` | Hello World | HELLO-WORLD-FUGAZI-17 |
| hello-18 | `{"greeting":"Hello World","worker":"18"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-3 | 1/1 pass | true | true | `12a7d9167dc7…` | `12a7d9167dc7…` | Hello World | HELLO-WORLD-FUGAZI-18 |
| hello-19 | `{"greeting":"Hello World","worker":"19"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-1 | 1/1 pass | true | true | `1a9a2ff28ad6…` | `1a9a2ff28ad6…` | Hello World | HELLO-WORLD-FUGAZI-19 |
| hello-20 | `{"greeting":"Hello World","worker":"20"}` | primary | 1 | medium (selected) | codex/sdk | openai/gpt-5.6-sol | oauth | central_broker | chatgpt-oauth-2 | 1/1 pass | true | true | `99eb4e777135…` | `99eb4e777135…` | Hello World | HELLO-WORLD-FUGAZI-20 |

_Generated from the run JSONL by Fugazi. Full 64-hex digests available in the source JSONL._
