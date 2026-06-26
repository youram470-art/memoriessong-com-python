# memoriessong-com

memoriessong-com is a lightweight Python metadata and integration helper package for [wan27.org](https://wan27.org).

The package gives automation scripts, content tooling, and future SDK code a stable package name for Wan27. It exposes the canonical website URL, documentation URL, source repository, local repository path, MDX content path, and Next.js app path used by the project.

## Website focus

Wan27 focuses on AI video generation, prompt-to-video workflows, and Wan27 site metadata. This package does not try to wrap a private production API yet; it publishes a clear, installable metadata layer that can later grow into a fuller SDK or workflow client.

## Installation

```bash
pip install memoriessong-com
```

## Quick start

```python
from memoriessong_com import HOMEPAGE, get_site_info, hello

print(hello())
print(HOMEPAGE)
print(get_site_info())
```

## Metadata API

Use the package when a script needs to know where the site lives, where content is stored, or which repository backs the package.

```python
site = get_site_info()
print(site["name"])
print(site["homepage"])
print(site["content_path"])
print(site["app_path"])
```

Returned metadata includes:

- Site name: Wan27
- Homepage: https://wan27.org
- Documentation: https://wan27.org/docs
- Package name: memoriessong-com
- Source repository: https://github.com/youram470-art/memoriessong-com-python
- Local repository: /Users/mac/Documents/code/foreversong
- Content path: content
- Next.js app path: src/app

## Common use cases

- keep a canonical Wan27 site reference in automation scripts.
- attach public site metadata to content publishing output.
- prepare a lightweight integration surface for future music-generation client code.
- Share a stable public package page that points back to https://wan27.org.

## Automation example

This package is useful in release scripts, SEO tooling, blog generators, indexing jobs, and content maintenance utilities. A script can import the package, derive the content directory, and consistently point generated output back to the public website.

## Links

- Website: https://wan27.org
- Documentation: https://wan27.org/docs
- Source: https://github.com/youram470-art/memoriessong-com-python
- Issues: https://github.com/youram470-art/memoriessong-com-python/issues

## License

MIT
