Name:		init-headphone
Version:	0.2.0
Release:	1%{?dist}
Summary:	Reactivates the headphone jack on Clevo W230SS after suspend

License:	GPLv2
URL:		https://bugs.launchpad.net/ubuntu/+source/alsa-driver/+bug/1313904/
Source0:	https://github.com/letitz/%{name}/archive/master.tar.gz

BuildArch:  noarch

BuildRequires: systemd
Requires:	i2c-tools-python
Requires:   systemd

%description
This script fixes a bug in Clevo W230SS-based laptops where the headphone jack
would not work anymore after a resume from suspend.

%prep
%setup -qn %{name}-master


%build



%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/init-headphone
%{_sysconfdir}/sysconfig/modules/init-headphone.modules
%{_unitdir}/init-headphone.service

%changelog

