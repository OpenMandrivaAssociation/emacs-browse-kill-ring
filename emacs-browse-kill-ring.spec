%define rname browse-kill-ring

Summary:	Interactively insert items from kill-ring
Name:		emacs-%{rname}
Version:	1.3
Release:	11
License:	GPLv2+
Group:		Editors
Url:		https://www.todesschaf.org/projects/bkr.html
Source0:	%{rname}.el
Source1:	%{name}-autostart.el
BuildRequires:	emacs
BuildRequires:	perl
BuildArch:	noarch

%description
Ever feel that 'C-y M-y M-y M-y ...' is not a great way of trying
to find that piece of text you know you killed a while back?  Then
browse-kill-ring is for you.

%files
%doc DOCUMENTATION
%config(noreplace) /etc/emacs/site-start.d/%{name}.el
%{_datadir}/*/site-lisp/*el*

#----------------------------------------------------------------------------

%prep
%setup -T -c
install -m644 %{SOURCE0} .

%build
emacs -batch -q -no-site-file -f batch-byte-compile %{rname}.el
mv %{rname}.elc emacs-%{rname}.elc

#Maybe need adjust
perl -n -e 'last if /^\(/;last if /^;;; Code/; s|^([;])+\s||; print' < %{SOURCE0} > DOCUMENTATION

%install
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
install -m644 emacs-%{rname}.elc %{buildroot}%{_datadir}/emacs/site-lisp/
install -m644 %{rname}.el %{buildroot}%{_datadir}/emacs/site-lisp/

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el

