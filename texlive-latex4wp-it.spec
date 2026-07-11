%global tl_name latex4wp-it
%global tl_revision 36000

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.10
Release:	%{tl_revision}.1
Summary:	LaTeX guide for word processor users, in Italian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex4wp-it
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp-it.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp-it.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a version of the document in Italian

