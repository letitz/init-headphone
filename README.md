# init-headphone
Fedora package for init-headphone.

Re-enables the headphone jack after sleep/suspend resume on Clevo W230SS-based
laptops.

## Installation

Download the latest RPM from [here](https://github.com/letitz/init-headphone/releases), or from the command line:
```sh
$ wget https://github.com/letitz/init-headphone/releases/download/0.2.0/init-headphone-0.2.0-1.fc21.noarch.rpm
```

Install it:
```sh
$ sudo dnf install init-headphone-*.rpm
```

Add `acpi_enforce_resources=lax` to `GRUB_COMMAND_LINE_LINUX` in
`/etc/default/grub`.

You're all set! Try suspending and resuming and enjoy the sound in your
headphones!

## Credits

Unrud for finding the fix, writing the script and packaging it for Debian

Ektor5 for packaging it for Arch Linux

### Sources and discussions:
- https://bugzilla.kernel.org/show_bug.cgi?id=75151
- https://bugs.launchpad.net/ubuntu/+source/alsa-driver/+bug/1313904/

