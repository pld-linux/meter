Summary:	Mete out time to a child process
Summary(pl.UTF-8):	Wymierzanie czasu procesowi potomnemu
Name:		meter
Version:	0.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://cyberknights.com.au/software/meter/%{name}-%{version}.tar.gz
# Source0-md5:	a807f0081e6ff7277cd0ec8c37c5c52d
URL:		http://cyberknights.com.au/software/meter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small utility to terminate child process after specified amount of
time.

%description -l pl.UTF-8
Małe narzędzie do zakończenia procesu potomnego po upłynięciu
określonego czasu.

%prep
%setup -q -c

%build
rm -f meter

%{__make} meter \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install meter $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
