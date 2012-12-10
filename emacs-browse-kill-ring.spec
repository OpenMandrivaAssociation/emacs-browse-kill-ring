%define rname browse-kill-ring

%define flavor emacs xemacs

Summary:	Interactively insert items from kill-ring
Name:		emacs-%{rname}
Version:	1.3
Release:	%mkrel 9
Source0:	%{rname}.el
Source1:	%{name}-autostart.el
License:	GPLv2+
Group:		Editors
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	%{flavor}
BuildRequires:	emacs-bin
BuildRequires:	perl
BuildArch:	noarch
URL:		http://www.todesschaf.org/projects/bkr.html

%description
Ever feel that 'C-y M-y M-y M-y ...' is not a great way of trying
to find that piece of text you know you killed a while back?  Then
browse-kill-ring is for you.

%prep
mkdir -p %{name}-%{version}/
install -m644 %{SOURCE0} %{name}-%{version}/
%setup -T -D

%build
for i in %{flavor};do
$i -batch -q -no-site-file -f batch-byte-compile %{rname}.el 
mv %{rname}.elc $i-%{rname}.elc
done

#Maybe need adjust
perl -n -e 'last if /^\(/;last if /^;;; Code/; s|^([;])+\s||; print' < %{SOURCE0} > DOCUMENTATION

%install
rm -rf %{buildroot}

for i in %{flavor};do
mkdir -p %{buildroot}%{_datadir}/$i/site-lisp/
install -m644 $i-%{rname}.elc %{buildroot}%{_datadir}/$i/site-lisp/
[[ $i = emacs ]] && mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
[[ $i = emacs ]] && install -m644 %{rname}.el %{buildroot}%{_datadir}/emacs/site-lisp/
done

install -d %buildroot%{_sysconfdir}/emacs/site-start.d
cat << EOF > %buildroot%{_sysconfdir}/emacs/site-start.d/%{name}.el
%{expand:%(%__cat %{SOURCE1})}
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc DOCUMENTATION
%config(noreplace) /etc/emacs/site-start.d/%{name}.el
%{_datadir}/*/site-lisp/*el*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-9mdv2011.0
+ Revision: 618047
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3-8mdv2010.0
+ Revision: 428555
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-7mdv2009.0
+ Revision: 244697
- rebuild

* Fri Feb 15 2008 Adam Williamson <awilliamson@mandriva.org> 1.3-5mdv2008.1
+ Revision: 168717
- rebuild for new era
- new URL
- new license policy
- minor spec clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import emacs-browse-kill-ring


* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-4mdk
- rebuild for latest emacs

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-3mdk
- rebuild

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-2mdk
- rebuild for latest emacs

* Tue Jan 14 2003 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3-1mdk
- Adjust Documentation generation.
- Bump to version 1.3.

* Fri Jun 21 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0-2mdk
- replace Copyright by License
- add URL
- buildarch noarch
- buildrequires emacs-bin

* Tue Oct  2 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-1mdk
- 1.0.

* Tue May 29 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8-1mdk
- First version.


# end of file
