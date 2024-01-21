# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Explicit `.readthedocs.yaml` config file, now required by RTD.

### Changed
- Broaden `HeartbeatFieldValue` type to allow both `int` and `float` values in the same tuple.
- Accept more abstract `Sequence` types (rather than strict `List` types) in `logging` functions.
- Project metadata now specified entirely in `pyproject.toml`, requiring `setuptools >= 61.0.0`.

### Fixed
- README: conda package installation command.
- examples: `field_with_normalization` using old keyword arguments for `logging.get_log_records`.


## [0.1.1] - 2023-06-21

### Added
- Installation and Getting Started instructions in Sphinx documentation.

### Fixed
- Improved Python type hints.


## [0.1.0] - 2021-12-15

### Added
- Publish documentation on [Read the Docs](https://apphb-python.readthedocs.io/).
- Optional parameters in `logging.get_log_record` and `logging.get_log_records`: `time_norm`, `heartrate_norm`, `field_norms`, and `field_rate_norms`.

### Changed
- Optional parameter design in `logging.get_log_record` and `logging.get_log_records` to separate time-specific values, which aligns with the design of other submodule functions and class methods.

### Removed
- Optional parameters in `logging.get_log_record` and `logging.get_log_records`: `norm` and `rate_norm`.


## [0.0.1] - 2021-11-15

- Initial release

[Unreleased]: https://github.com/libheartbeats/apphb-python/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/libheartbeats/apphb-python/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/libheartbeats/apphb-python/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/libheartbeats/apphb-python/releases/tag/v0.0.1
