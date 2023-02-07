# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2022-2-6

### Added

- This changelog file.
- Achievement class.
- Pyproject.toml for tbump and pytest configs.
- Return documentation on dataclass class methods.
- More tests.
- More documentation on Client methods.

### Changed

- Documentation wording.

### Removed

- hypixel.version_info.
- models.Friend (deprecated by hypixel).
- Client.player_friends (deprecated by hypixel).
- Player.version.
- Random print statement.

### Fixed

- Documentation punctuation.
- Version locking in setup.py.
- Circular import bug.
- Readthedocs config formatting.

### Breaking Changes

- Status.game_type is changed to Status.game.

## [0.3.1] - 2022-10-16

### Fixed

- Datetimes are now properly in UTC time rather than local time.
- Datetime tests are now fixed and enabled.
- Documentation links now go to latest rather than dev (a deleted version).

### Deprecated

- Player.version always returns ``None`` and will be removed in a later release.

[Unreleased]: https://github.com/duhby/hypixel.py/compare/v0.4.0...master
[0.4.0]: https://github.com/duhby/hypixel.py/releases/tag/v0.4.0
[0.3.1]: https://github.com/duhby/hypixel.py/releases/tag/v0.3.1
