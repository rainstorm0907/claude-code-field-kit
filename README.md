# claude-code-field-kit

클로드 코드에서 바로 쓰는 스킬 묶음이야. 뭘 만들지 생각을 정리하고, 코드를 단단하게 짜고, 작업을 깔끔하게 마무리하는 쪽에 힘을 줬어.

## 설치

```bash
git clone https://github.com/rainstorm0907/claude-code-field-kit.git
cd claude-code-field-kit && ./install.sh
```

| 넣는 것 | 어디로 |
|---|---|
| `skills/*` | `~/.claude/skills/` |

- 기본은 심링크라서 나중에 `git pull`만 하면 갱신돼. 복사로 넣고 싶으면 `./install.sh --copy`.
- 같은 이름의 스킬이 이미 있으면 지우지 않고 `~/.claude/backup-field-kit-<시각>/`으로 옮겨 둬.
- 설치 뒤 새 클로드 코드 세션을 열면 잡혀.

## 스킬

| 묶음 | 스킬 | 언제 |
|---|---|---|
| 생각·프레임 | `discusser` | 아직 뭘 정해야 할지 모를 때, 중요한 선택을 비교할 때 |
| | `product-framing` | 제품·공모전 결과물에 다음으로 뭘 걸지 정할 때 |
| | `metaframe` | 고칠수록 딴 데가 깨질 때, 지금 접근을 유지할지 바꿀지 |
| | `deep-dive` | 근거가 엇갈리거나 비어서 빠른 검색으로 안 풀릴 때 |
| 코딩 태도 | `laws` | 버그를 설계 실패로 보고 구조로 막을 때 |
| | `keep-simple` | 제일 작은 올바른 수정 |
| 문서·마무리 | `update-docs` | 대표 문서에 바뀐 상태 반영 |
| | `wrapping-sessions` | 작업 마무리, 다음 사람에게 넘길 기록 |
| | `pr-wrap` | PR 만들기·설명 갱신 |
| 도구 | `screenshot` | 데스크톱·앱 창 캡처 |
| | `find-skills` | 필요한 스킬 찾기 |

스킬은 설명이 상황에 맞으면 클로드가 알아서 읽어. 직접 부르려면 `/discusser`처럼 이름을 치면 돼.

## 같이 깔면 좋은 외부 스킬

남이 만든 거라 여기 복사하지 않고 원본 설치 경로만 적어 둘게.

| 스킬 | 하는 일 | 설치 |
|---|---|---|
| humanize-korean | AI 티 나는 한글을 사람 글처럼 윤문 | `/plugin marketplace add epoko77-ai/im-not-ai` 후 `/plugin install humanize-korean@im-not-ai` |
| insane-search | 막힌 사이트(X·Reddit·네이버 등) 우회 조회 | `/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git` 후 `/plugin install insane-search@gptaku-plugins` |
| stack-diagram | 로고 들어간 아키텍처 도식 | `npx skills add caru-ini/stack-diagram` |

`deep-dive`는 웹 조사할 때 Aside 같은 브라우징 스킬이 깔려 있으면 그걸 써.

## 고칠 때

- `python3 scripts/check.py`는 스킬끼리 거는 링크가 전부 이 묶음 안을 가리키는지 확인해.

`screenshot`은 OpenAI 공개 스킬을 클로드 코드용으로 고친 거라 Apache-2.0 라이선스(`skills/screenshot/LICENSE.txt`)를 따라.
