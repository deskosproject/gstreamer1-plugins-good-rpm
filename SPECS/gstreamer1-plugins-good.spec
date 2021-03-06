%global         majorminor      1.0

# Turn off extras package on RHEL.
%if ! 0%{?rhel}
%bcond_without extras
%else
%bcond_with extras
%endif

Name:           gstreamer1-plugins-good
Version:        1.4.5
Release:        2.1%{?dist}
Summary:        GStreamer plugins with good code and licensing

License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
Patch1:         0001-jitterbuffer-Allow-rtp-caps-without-clock-rate.patch
Patch2:         0001-tests-souphttpsrc-update-ssl-key-cert-pair.patch

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  flac-devel >= 1.1.4
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 1.2.0
BuildRequires:  libshout-devel
BuildRequires:  libsoup-devel
BuildRequires:  libX11-devel
BuildRequires:  orc-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speex-devel
BuildRequires:  taglib-devel
BuildRequires:  wavpack-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvpx-devel >= 1.1.0

%ifnarch s390 s390x
BuildRequires:  libavc1394-devel
BuildRequires:  libdv-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libraw1394-devel
%endif

# extras
%if %{with extras}
BuildRequires:  jack-audio-connection-kit-devel
%endif

# documentation
BuildRequires:  gtk-doc
BuildRequires:  python-devel


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


%if %{with extras}
%package extras
Summary:        Extra GStreamer plugins with good code and licensing
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description extras
GStreamer is a streaming media framework, based on graphs of filters
which operate on media data.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

%{name}-extras contains extra "good" plugins
which are not used very much and require additional libraries
to be installed.
%endif


%prep
%setup -q -n gst-plugins-good-%{version}
%patch1 -p1
%patch2 -p1

%build
%configure \
  --with-package-name='Fedora GStreamer-plugins-good package' \
  --with-package-origin='http://download.fedoraproject.org' \
  --enable-experimental \
  --enable-gtk-doc \
  --enable-orc \
  --disable-monoscope \
  --disable-aalib \
  --disable-cairo \
  --disable-libcaca \
%if %{with extras}
  --enable-jack \
%else
  --disable-jack \
%endif
  --with-default-visualizer=autoaudiosink
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang gst-plugins-good-%{majorminor}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Fix CVE-2016-9634, CVE-2016-9635, CVE-2016-9636
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so

%files -f gst-plugins-good-%{majorminor}.lang
%doc AUTHORS COPYING README REQUIREMENTS
%doc %{_datadir}/gtk-doc/html/gst-plugins-good-plugins-%{majorminor}

# Equaliser presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstVP8Enc.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstIirEqualizer3Bands.prs

# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstalaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstalphacolor.so
%{_libdir}/gstreamer-%{majorminor}/libgstalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstapetag.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofx.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{majorminor}/libgstauparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstautodetect.so
%{_libdir}/gstreamer-%{majorminor}/libgstavi.so
%{_libdir}/gstreamer-%{majorminor}/libgstcutter.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebug.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtmf.so
%{_libdir}/gstreamer-%{majorminor}/libgsteffectv.so
%{_libdir}/gstreamer-%{majorminor}/libgstequalizer.so
%{_libdir}/gstreamer-%{majorminor}/libgstflv.so
#%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom.so
%{_libdir}/gstreamer-%{majorminor}/libgsticydemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3demux.so
%{_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterleave.so
%{_libdir}/gstreamer-%{majorminor}/libgstisomp4.so
%{_libdir}/gstreamer-%{majorminor}/libgstlevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstmatroska.so
%{_libdir}/gstreamer-%{majorminor}/libgstmulaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultifile.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultipart.so
%{_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{majorminor}/libgstoss4audio.so
%{_libdir}/gstreamer-%{majorminor}/libgstreplaygain.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstshapewipe.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmpte.so
%{_libdir}/gstreamer-%{majorminor}/libgstspectrum.so
%{_libdir}/gstreamer-%{majorminor}/libgstudp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideobox.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideocrop.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so

# gstreamer-plugins with external dependencies but in the main package
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstossaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpng.so
%{_libdir}/gstreamer-%{majorminor}/libgstpulse.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{majorminor}/libgstshout2.so
%{_libdir}/gstreamer-%{majorminor}/libgstsouphttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeex.so
%{_libdir}/gstreamer-%{majorminor}/libgsttaglib.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvpx.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so

%ifnarch s390 s390x
%{_libdir}/gstreamer-%{majorminor}/libgstdv.so
%{_libdir}/gstreamer-%{majorminor}/libgst1394.so
%endif


%if %{with extras}
%files extras
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstjack.so
%endif


%changelog
* Tue Nov 29 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.4.5-2.1
- Fix CVE-2016-9634, CVE-2016-9635, CVE-2016-9636 by removing libgstflxdec.so
- Rebuilt for DeskOS

* Tue Jun 23 2015 Wim Taymans <wtaymans@redhat.com> - 1.4.5-2
- update SSL certificates in unit test
- Resolves: #1174398

* Wed Jan 28 2015 Bastien Nocera <bnocera@redhat.com> - 1.4.5-1
- Update to 1.4.5
- Resolves: #1174398

* Thu Feb  6 2014 Wim Taymans <wtaymans@redhat.com> - 1.0.7-5
- Fix wrong reference in docs (#884492)
- Disable the cairo plugin, we don't package it (#1048513)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.0.7-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.7-3
- Mass rebuild 2013-12-27

* Mon Nov  4 2013 Matthias Clasen <mclasen@redhat.com> - 1.0.7-2
- Rebuild with new gtk-doc to fix multilib conflict
- Related: #884492

* Fri Apr 26 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7.

* Sun Mar 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6.
- Drop BR on PyXML.

* Wed Feb  6 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.5-3
- Add gdk-pixbuf2-devel build dep. It was pulled in by something else for gst 0.10

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.5-2
- rebuild due to "jpeg8-ABI" feature drop

* Tue Jan  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Wed Dec 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Nov 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Drop speexdec patch. Fixed upstream.
- Drop vp8 patches. Fixed upstream.

* Wed Nov  7 2012 Debarshi Ray <rishi@fedoraproject.org> - 1.0.2-3
- Fixes for GNOME #687464 and #687793

* Fri Nov  2 2012 Debarshi Ray <rishi@fedoraproject.org> - 1.0.2-2
- Fixes for vp8dec including GNOME #687376

* Thu Oct 25 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
- Drop upstream patches since they are included in latest release.

* Wed Oct 24 2012 Debarshi Ray <rishi@fedoraproject.org> - 1.0.1-2
- Fix target-bitrate for vp8enc

* Sun Oct  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Tue Oct  2 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-3
- Add required version for vpx-devel. (#862157)

* Mon Oct  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-2
- Enable verbose build

* Mon Sep 24 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0.

* Fri Sep 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.99-2
- Add vp8 plugin to package from gst1-plugins-bad. (#859505)

* Wed Sep 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.99-1
- Update to 0.11.99

* Fri Sep 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.94-1
- Update to 0.11.94.
- Drop v4l2-buffer patch. Fixed upstream.

* Wed Aug 15 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.93-1
- Update to 0.11.93.
- Add batch to fix build with recent kernels, the v4l2_buffer input field was removed.
- Use %%global instead of %%define.

* Wed Jul 18 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.92-1
- Initial Fedora spec.
