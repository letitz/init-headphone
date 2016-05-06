Name:		init-headphone
Version:	0.10
Release:	1%{?dist}
Summary:	Reactivates the headphone jack on some Clevo laptops after suspend

License:	GPLv3
URL:		https://github.com/letitz/%{name}

%global commit 843da720f3531a0ae6860130c5baa1f8e2ba7d1b
Source0:	https://github.com/letitz/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:  noarch

%{?systemd_requires}
BuildRequires: systemd
Requires:	i2c-tools-python

%description
This script fixes a bug in Clevo W230SS-based laptops where the headphone jack
would not work anymore after a resume from suspend.

%prep
%setup -qn %{name}-%{commit}

%build

%install
%make_install

%post
%systemd_post init-headphone.service

%preun
%systemd_preun init-headphone.service

%postun
%systemd_postun_with_restart init-headphone.service

%files
%{_sbindir}/init-headphone
%{_sysconfdir}/modules-load.d/init-headphone.conf
%{_unitdir}/init-headphone.service

%changelog

