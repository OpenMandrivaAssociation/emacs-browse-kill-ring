%define rname browse-kill-ring

%define flavor emacs xemacs

Summary:	Interactively insert items from kill-ring
Name:		emacs-%{rname}
Version:	1.3
Release:	%mkrel 7
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

