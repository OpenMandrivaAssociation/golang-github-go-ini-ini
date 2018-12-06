# http://github.com/go-ini/ini
%global goipath         github.com/go-ini/ini
Version:                1.39.0

%gometa

%global v1_goipath     gopkg.in/v1/ini
%global v1_goipath_sec gopkg.in/ini.v1

%global v1_goipath_name %gorpmname %{v1_goipath}
%global v1_goipath_sec_name %gorpmname %{v1_goipath_sec}

Name:           golang-github-go-ini-ini
Release:        1%{?dist}
Summary:        Package ini provides INI file read and write functionality in Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/smartystreets/goconvey/convey)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%package -n %{v1_goipath_name}-devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/smartystreets/goconvey/convey)

%description -n %{v1_goipath_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{v1_goipath} prefix.

%package -n %{v1_goipath_sec_name}-devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/smartystreets/goconvey/convey)

%description -n %{v1_goipath_sec_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{v1_goipath_sec} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml
%goinstall glide.lock glide.yaml -i %{v1_goipath} -o v1-devel.file-list
%goinstall glide.lock glide.yaml -i %{v1_goipath_sec} -o v1-sec-devel.file-list

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%files -n %{v1_goipath_name}-devel -f v1-devel.file-list
%license LICENSE
%doc README.md

%files -n %{v1_goipath_sec_name}-devel -f v1-sec-devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.39.0-1
- Update to release 1.39.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.21.1-0.10.20170628git3d73f4b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-0.9.git3d73f4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.21.1-0.8.git3d73f4b
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.21.1-0.7.20170628git3d73f4b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-0.6.git3d73f4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.21.1-0.5.git3d73f4b
- Bump to upstream 3d73f4b845efdf9989fffd4b4e562727744a34ba
  related: #1412590

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-0.4.git6e4869b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-0.3.git6e4869b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-0.2.git6e4869b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.21.1-0.1.git6e4869b
- Bump to upstream 6e4869b434bd001f6983749881c7ead3545887d8
  resolves: #1412590

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-0.2.git193d1ec
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 1.9.0-0.1.git193d1ec
- First package for Fedora
  resolves: #1327497
