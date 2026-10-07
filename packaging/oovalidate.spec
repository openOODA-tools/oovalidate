Name:           oovalidate
Version:        0.1.0
Release:        1%{?dist}
Summary:        Validates JSON, YAML, and XML documents against JSON Schema draft 2020-12.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oovalidate
Source0:        oovalidate-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oovalidate is a sovereign, capability-bounded SCHEMA CHECKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oovalidate
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oovalidate-uninstall

%files
/usr/bin/oovalidate
/usr/bin/oovalidate-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
