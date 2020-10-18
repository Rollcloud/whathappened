[![GitHub license](https://img.shields.io/github/license/Rollcloud/whathappened)](https://github.com/Rollcloud/whathappened/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Rollcloud/whathappened/test-build?logo=github)](https://github.com/Rollcloud/whathappened/actions?query=workflow%3Atest-build)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whathappened?logo=pypi)](https://pypi.org/project/whathappened/)
[![semver](https://img.shields.io/badge/semver-2.0.0-blue)](https://semver.org/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/rollcloud/whathappened?sort=semver)](https://github.com/Rollcloud/whathappened/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# whathappened
A changelog generator using simply structured git commit messages

## Inspired by

* [SemVer](https://semver.org/)
* [Angular Commit Message Format](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)
* [Auto Changelog](https://github.com/Michael-F-Bryan/auto-changelog)
* [git_commits.py](https://gist.github.com/simonw/091b765a071d1558464371042db3b959#file-get_commits-py)

## Install and Run

Installation is as simple as it gets:

    $ pip install whathappened

~~To generate a changelog, run:~~

    $ whathappened

Make sure to activate any virtual envrionment that you might be using first.

## Package Changelog

Created by Whathappened itself - very meta.

For the complete changelog, please see [CHANGELOG.md](CHANGELOG.md).

## Whathappened Commit Message Format

Whathappened expects git commit messages in the format outlined below:

    [optional breaking ]<type>[ optional (<scope>)]: <description>

    [optional body]

`<type>` is recommended to be one of:

    fix
    feat
    build
    chore
    ci
    docs
    style
    refactor
    perf
    test

`<scope>` is recommended to be a module, file, or folder name as appropiate.

### Examples

All of the examples below are acceptable commit message formats:

The simplest message:

    style: isn't it neat

Defining scope:

    docs(gadgets): remember the gizmos

Signalling a breaking change

    breaking feat: add the whozits

Defining scope, including a space:

    fix (whatsits): repair the thingamabobs

Multiple lines:

    test: How many have I got?

    I've got twenty
    But who cares?

    I want more

For more examples, please see whathappened's [commits](https://github.com/Rollcloud/whathappened/commits/).

This is a simpler version of https://www.conventionalcommits.org/
