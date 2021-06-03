VERSION=0.5
INSTALL=/usr/bin/install -c

mandir?=${DESTDIR}/opt/flaccda/man
man1dir?=$(mandir)/man1
bindir?=${DESTDIR}/opt/flaccda/bin
profile?=${DESTDIR}/etc/profile.d

.PHONY:
	echo 'Did you read the README?'

.PHONY: tar
tar:
	@cd .. && tar czvf flaccda-$(VERSION).tar.gz \
	flaccda-$(VERSION)/{ChangeLog,flaccda.{spec,SlackBuild},slack-desc,makefile,NOTICE,README,version.sh,src/{flaccda,mp3cda,stripmb},man/flaccda.1,flaccda.sh}

.PHONY: rpm
rpm: tar
	@cd .. && rpmbuild -ta flaccda-$(VERSION).tar.gz

install:
	$(INSTALL) -d -m 755 $(bindir)
	$(INSTALL) -m 755 src/flaccda $(bindir)
	$(INSTALL) -m 755 src/mp3cda $(bindir)
	$(INSTALL) -m 755 src/stripmb $(bindir)
	$(INSTALL) -d -m 755 $(man1dir)
	$(INSTALL) -m 644 man/flaccda.1 $(man1dir)/flaccda.1
	$(INSTALL) -d -m 755 $(profile)
	$(INSTALL) -m 755 flaccda.sh $(profile)/flaccda.sh

uninstall:
	rm -f $(bindir)/{flaccda,mp3cda,stripmb}
	rm -f $(mandir)/man1/flaccda.1
	rm -f $(profile)/flaccda.sh
