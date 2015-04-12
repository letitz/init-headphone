SBINDIR=usr/sbin
SYSCONFIGDIR=etc
LIBDIR=usr/lib

all:

install:
	install -Dm 755 init-headphone ${DESTDIR}/${SBINDIR}/init-headphone
	install -Dm 755 init-headphone.modules ${DESTDIR}/${SYSCONFIGDIR}/sysconfig/modules/init-headphone.modules
	install -Dm 755 init-headphone.service ${DESTDIR}/${LIBDIR}/systemd/system/init-headphone.service
	systemctl enable init-headphone

