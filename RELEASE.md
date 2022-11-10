# Release information

## make release
* update release notes in `release-notes` with commit
* make sure all tests run (`tox -p`)
* bump version (`bumpversion [major|minor|patch]`)
* `git push --tags` (triggers release)

* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.10
(test) pip install pymetadata
```


