# Exercism Solutions

This repository stores Exercism solutions grouped by track under `solutions/`.
Each track directory uses the Exercism track slug, and each exercise keeps the
standard Exercism exercise layout.

## Layout

```text
solutions/
  bash/
  elisp/
  elixir/
  go/
  java/
  python/
```

Exercise directories live one level below their track:

```text
solutions/python/hello-world/
solutions/java/two-fer/
solutions/bash/two-fer/
```

`solutions/go` is currently a placeholder for future Go exercises. The folder
name is `go` to match the Exercism track slug.

## Running Tests Locally

Run tests from the exercise or track directory, depending on the language:

```sh
cd solutions/python
python -m pip install -r requirements.txt
python -m pytest
```

```sh
cd solutions/java/hello-world
gradle test
```

```sh
cd solutions/bash/hello-world
bats hello_world_test.sh
```

```sh
cd solutions/elixir/hello-world
elixir hello_world_test.exs
```

```sh
cd solutions/elisp/hello-world
emacs --batch -l hello-world-test.el -f ert-run-tests-batch-and-exit
```

```sh
cd solutions/go/<exercise>
go test ./...
```

## CI

GitHub Actions is configured in `.github/workflows/test.yml`.

On pushes to `master` and pull requests, the workflow detects which
`solutions/<track>/` folders changed and only runs tests for those tracks.
Changing the workflow file runs every configured language job.
