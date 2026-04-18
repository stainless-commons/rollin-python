# Changelog

## 0.1.0 (2026-04-18)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/stainless-commons/rollin-python/compare/v0.0.2...v0.1.0)

### Features

* **internal:** implement indices array format for query and form serialization ([5132e59](https://github.com/stainless-commons/rollin-python/commit/5132e597c589409785472b639bbffd1866c29234))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([2db1259](https://github.com/stainless-commons/rollin-python/commit/2db1259652670d03d353c982a5fcb88ff97948eb))
* **deps:** bump minimum typing-extensions version ([248d6e1](https://github.com/stainless-commons/rollin-python/commit/248d6e1ec3187b8f0ab1354546f438b028206539))
* ensure file data are only sent as 1 parameter ([c0cfd97](https://github.com/stainless-commons/rollin-python/commit/c0cfd9728ca956c2a3b803d49039e815696aa2b8))
* **pydantic:** do not pass `by_alias` unless set ([46606d7](https://github.com/stainless-commons/rollin-python/commit/46606d71ab95ee25148a1f3d328cb99b071e5985))
* sanitize endpoint path params ([4cac545](https://github.com/stainless-commons/rollin-python/commit/4cac545783e2a3d350953f3b630ad4184c9a2142))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([78f42c3](https://github.com/stainless-commons/rollin-python/commit/78f42c3ee397ab5d7e54ca2257b3a00577e55b7d))


### Chores

* **ci:** bump uv version ([e2553be](https://github.com/stainless-commons/rollin-python/commit/e2553be28eaf15c6dba43a69bf18ef21da13c2c2))
* **ci:** skip lint on metadata-only changes ([5de7de3](https://github.com/stainless-commons/rollin-python/commit/5de7de3d905ee01b56ca1510c1bd2ae54c14b320))
* **ci:** skip uploading artifacts on stainless-internal branches ([15bab4f](https://github.com/stainless-commons/rollin-python/commit/15bab4f9dd2202e7c59db7eb989357a66add5c99))
* **internal:** add request options to SSE classes ([77a8a4f](https://github.com/stainless-commons/rollin-python/commit/77a8a4f9e5e163723ec76f0e5ec36cc31d95de8d))
* **internal:** make `test_proxy_environment_variables` more resilient ([548c10c](https://github.com/stainless-commons/rollin-python/commit/548c10c5c391e4a6af20894be87877a7f155b152))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([12600f1](https://github.com/stainless-commons/rollin-python/commit/12600f143df64f57dafcc0d6b09786d6307ddbe5))
* **internal:** refactor authentication internals ([48125d3](https://github.com/stainless-commons/rollin-python/commit/48125d30130615b923c515aed42b0a42b1a57776))
* **internal:** remove mock server code ([7487832](https://github.com/stainless-commons/rollin-python/commit/748783209dbc1f1157a739d2020da3bf32946b8e))
* **internal:** tweak CI branches ([de75be7](https://github.com/stainless-commons/rollin-python/commit/de75be7056967b0037326c66135e542322cea8cd))
* **internal:** update gitignore ([9aca850](https://github.com/stainless-commons/rollin-python/commit/9aca85013a1c6977ba12ce4c3d4f9a796c970d19))
* update mock server docs ([f0c9141](https://github.com/stainless-commons/rollin-python/commit/f0c914149e0b63378b1e61939d99ea69065715e6))

## 0.0.2 (2026-02-16)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/stainless-commons/rollin-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([8d66666](https://github.com/stainless-commons/rollin-python/commit/8d66666ef5c1b60ac7765ccabcb8a6d14f1acfc8))
* update SDK settings ([6997733](https://github.com/stainless-commons/rollin-python/commit/6997733f513985b8b46ec7d21a8dca5572756f97))
