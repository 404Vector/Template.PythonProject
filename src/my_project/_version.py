from importlib_metadata import version, PackageNotFoundError

package_name = __name__.split(".")[0]

try:
    __version__ = version(package_name)
except PackageNotFoundError:
    __version__ = "unknown"
