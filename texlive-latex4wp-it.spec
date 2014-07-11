# revision 22335
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-latex4wp-it
Version:	20111103
Release:	8
Summary:	TeXLive latex4wp-it package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp-it.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive latex4wp-it package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/COME-COMPORRE
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/README
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/dat2tex
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/exa.sty
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/gnuplot.gp
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/gnuplot.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/latex4wp-it.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/latex4wp-it.tex
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/midifile.mid
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/small.eepic
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/small.eps
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/small.fig
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/small.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/small.pdf_t
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/tbx.epsi
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/tbx.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/tbx.tex
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/xfig.eps
%doc %{_texmfdistdir}/doc/latex/latex4wp-it/xfig.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 753132
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718811
- texlive-latex4wp-it
- texlive-latex4wp-it
- texlive-latex4wp-it
- texlive-latex4wp-it

