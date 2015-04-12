SBINDIR=usr/sbin
SYSCONFIGDIR=etc
UNITDIR=usr/lib/systemd/system

all:

install:
	install -Dm 755 init-headphone ${DESTDIR}/${SBINDIR}/init-headphone
	install -Dm 755 init-headphone.modules ${DESTDIR}/${SYSCONFIGDIR}/sysconfig/modules/init-headphone.modules
	install -Dm 755 init-headphone.service ${DESTDIR}/${UNITDIR}/init-headphone.service
	systemctl enable init-headphone

