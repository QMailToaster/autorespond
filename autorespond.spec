Name:       autorespond
Summary:    Simple autoresponder for qmail
Version:    2.0.5
Release:    0%{?dist}
License:    GPL
Group:      System/Servers
Vendor:     QmailToaster
Packager:   Eric Shubert <qmt-build@datamatters.us>
URL:	    http://www.inter7.com/index.php?page=development
Source:     http://www.inter7.com/devel/%{name}-%{version}.tar.gz
Obsoletes:  autorespond-toaster
BuildRoot:  %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define   debug_package %{nil}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
Mail is sent to help@my-company.com.   An automatically generated response
is sent back to the user  with an  address  of "help@my-company.com".  You
can set the  envelope  sender  to an empty string.  However, some programs
will parse the  message  for  the  "From:"  field and send an autoresponse
back to it.  It is received at your autoresponder, and you now have a mail
loop. 

This autoresponder  also catches some other simple situations such as mail
from a mailer-daemon, empty envelope sender, bulk precedence headers, etc.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------
gcc %{optflags} -Wall -o %{name} %{name}.c

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
rm -rf %{buildroot}
install -d %{buildroot}/%{_bindir}
install -m755 %{name} %{buildroot}/%{_bindir}/%{name}

#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------
%defattr(-,-,root)
%attr(0755,root,root) %{_bindir}/%{name}

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Nov 15 2013 Eric Shubert <eric@datamatters.us> 2.0.5
- Set up on github
- Added CentOS 6 support
- Removed unsupported cruft
- Dropped -toaster designation
* Wed Feb 29 2012 Bharath Chari <qmailtoaster@arachnis.com> 2.0.5.1.4.0
- Rebuilt with autoresponder 2.0.5
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.6
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.4
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.4
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.3.3
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 2.0.4-1.3.2
- Add Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.9
- Add Fedora Core 5 support
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.8
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.7
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.6
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.5
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 2.0.4-1.2.4
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.3
- Add Fedora Core 3 support
- Add CentOS 4 support
* Fri Jun 04 2004 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.2
- Udpate to autorespond 2.0.4
* Thu Jun 03 2004 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.8
- Add Fedora Core 2 support
* Mon Dec 29 2003 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.7
- Add Fedora Core 1 support
* Sun Nov 23 2003 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.6
- Add Trustix 2.0 support
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.5
- Clean-ups on SPEC file: compilation banner, better gcc detects
- Detect gcc-3.2.3
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Wed Apr 02 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.4
- Clean-ups
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.3
- Conectiva Linux 7.0 support
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0-1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sat Oct 05 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-0.9.2
- Soft clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
* Fri Sep 27 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.2.0.2-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.0.2-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.0.2-1
- New version: 0.7 toaster (rebuild with 0.7 spec)
* Thu Aug 13 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.6.2.0.2-1
- New version: 0.6 toaster.
* Mon Aug 12 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.5.2.0.2-1
- Checks for gcc-3.2 (default compiler from now)
- New version: 0.5 toaster.
* Tue Aug 08 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.4.2.0.2-1
- Rebuild against 0.4 toaster
* Thu Jul 30 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.2.0.2-2
- Now packages have got 'no sex': you can rebuild them with command line
  flags for specifics targets that are: RedHat, Trustix, and of course
  Mandrake (that is default)
* Sun Jul 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.2.0.2.1mdk
- toaster v. 0.3: now it is possible upgrading safely because of 'pversion'
  that is package version and 'version' that is toaster version
* Thu Jul 25 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-2.0.2.1mdk
- toaster v. 0.2
* Thu Jul 18 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-2.0.2.2mdk
- Added tests for gcc-3.1.1
- Added toaster version (we will need to mantain it too): is vtoaster 0.1
* Mon Jul 15 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1mdk
- First RPM package.
