Name:		init-headphone
Version:	0.2.0
Release:	1%{?dist}
Summary:	Reactivates the headphone jack on Clevo W230SS after suspend

License:	GPLv2
URL:		https://github.com/letitz/%{name}

%global commit 843da720f3531a0ae6860130c5baa1f8e2ba7d1b
Source0:	https://github.com/letitz/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:  noarch

BuildRequires: systemd
Requires:	i2c-tools-python
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
This script fixes a bug in Clevo W230SS-based laptops where the headphone jack
would not work anymore after a resume from suspend.

%prep
%setup -qn %{name}-%{commit}


%build



%install
make install DESTDIR=%{buildroot}

%post
%systemd_post init-headphone.service
systemctl enable init-headphone

%preun
systemctl disable init-headphone
%systemd_preun init-headphone.service

%postun
%systemd_postun

%files
%{_sbindir}/init-headphone
%{_sysconfdir}/sysconfig/modules/init-headphone.modules
%{_unitdir}/init-headphone.service

%changelog

