Name:		texlive-hang
Version:	43280
Release:	2
Summary:	Environments for hanging paragraphs and list items
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hang
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hang.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hang.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides environments for hanging paragraphs and
list items. In addition, it defines environments for labeled
paragraphs and list items.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hang
%doc %{_texmfdistdir}/doc/latex/hang

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
