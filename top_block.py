#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Aug  9 21:15:51 2021
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import lora_sdr
import pmt
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.sf_decode = sf_decode = 10
        self.bw = bw = 250000
        self.sf_4 = sf_4 = 8
        self.sf_3 = sf_3 = 7
        self.sf_2 = sf_2 = 10
        self.sf_1 = sf_1 = 9
        self.samp_rate = samp_rate = bw
        self.ruido = ruido = 0
        self.pay_len = pay_len = 64
        self.impl_head = impl_head = False
        self.has_crc = has_crc = True
        self.frame_period = frame_period = (2^sf_decode)/bw
        self.cr = cr = 4

        ##################################################
        # Blocks
        ##################################################
        self.lora_sdr_whitening_0_0_0_0 = lora_sdr.whitening()
        self.lora_sdr_whitening_0_0_0 = lora_sdr.whitening()
        self.lora_sdr_whitening_0_0 = lora_sdr.whitening()
        self.lora_sdr_whitening_0 = lora_sdr.whitening()
        self.lora_sdr_modulate_0_0_0_0 = lora_sdr.modulate(sf_4, samp_rate, bw)
        (self.lora_sdr_modulate_0_0_0_0).set_min_output_buffer(10000000)
        self.lora_sdr_modulate_0_0_0 = lora_sdr.modulate(sf_3, samp_rate, bw)
        (self.lora_sdr_modulate_0_0_0).set_min_output_buffer(10000000)
        self.lora_sdr_modulate_0_0 = lora_sdr.modulate(sf_2, samp_rate, bw)
        (self.lora_sdr_modulate_0_0).set_min_output_buffer(10000000)
        self.lora_sdr_modulate_0 = lora_sdr.modulate(sf_1, samp_rate, bw)
        (self.lora_sdr_modulate_0).set_min_output_buffer(10000000)
        self.lora_sdr_interleaver_0_0_0_0 = lora_sdr.interleaver(cr, sf_4)
        self.lora_sdr_interleaver_0_0_0 = lora_sdr.interleaver(cr, sf_3)
        self.lora_sdr_interleaver_0_0 = lora_sdr.interleaver(cr, sf_2)
        self.lora_sdr_interleaver_0 = lora_sdr.interleaver(cr, sf_1)
        self.lora_sdr_header_decoder_0 = lora_sdr.header_decoder(impl_head, cr, pay_len, has_crc)
        self.lora_sdr_header_0_0_0_0 = lora_sdr.header(impl_head, has_crc, cr)
        self.lora_sdr_header_0_0_0 = lora_sdr.header(impl_head, has_crc, cr)
        self.lora_sdr_header_0_0 = lora_sdr.header(impl_head, has_crc, cr)
        self.lora_sdr_header_0 = lora_sdr.header(impl_head, has_crc, cr)
        self.lora_sdr_hamming_enc_0_0_0_0 = lora_sdr.hamming_enc(cr, sf_4)
        self.lora_sdr_hamming_enc_0_0_0 = lora_sdr.hamming_enc(cr, sf_3)
        self.lora_sdr_hamming_enc_0_0 = lora_sdr.hamming_enc(cr, sf_2)
        self.lora_sdr_hamming_enc_0 = lora_sdr.hamming_enc(cr, sf_1)
        self.lora_sdr_hamming_dec_0 = lora_sdr.hamming_dec()
        self.lora_sdr_gray_enc_0 = lora_sdr.gray_enc()
        self.lora_sdr_gray_decode_0_0_0_0 = lora_sdr.gray_decode(sf_4)
        self.lora_sdr_gray_decode_0_0_0 = lora_sdr.gray_decode(sf_3)
        self.lora_sdr_gray_decode_0_0 = lora_sdr.gray_decode(sf_2)
        self.lora_sdr_gray_decode_0 = lora_sdr.gray_decode(sf_1)
        self.lora_sdr_frame_sync_0 = lora_sdr.frame_sync(samp_rate, bw, sf_decode, impl_head)
        self.lora_sdr_fft_demod_0 = lora_sdr.fft_demod(samp_rate, bw, sf_decode, impl_head)
        self.lora_sdr_dewhitening_0 = lora_sdr.dewhitening()
        self.lora_sdr_deinterleaver_0 = lora_sdr.deinterleaver(sf_decode)
        self.lora_sdr_crc_verif_0 = lora_sdr.crc_verif()
        self.lora_sdr_add_crc_0_0_0_0 = lora_sdr.add_crc(has_crc)
        self.lora_sdr_add_crc_0_0_0 = lora_sdr.add_crc(has_crc)
        self.lora_sdr_add_crc_0_0 = lora_sdr.add_crc(has_crc)
        self.lora_sdr_add_crc_0 = lora_sdr.add_crc(has_crc)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccf(4, (-0.128616616593872,	-0.212206590789194,	-0.180063263231421,	3.89817183251938e-17	,0.300105438719035	,0.636619772367581	,0.900316316157106,	1	,0.900316316157106,	0.636619772367581,	0.300105438719035,	3.89817183251938e-17,	-0.180063263231421,	-0.212206590789194,	-0.128616616593872))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_message_strobe_0_0_0_0 = blocks.message_strobe(pmt.intern("para diferentes pessoas "), 2000)
        self.blocks_message_strobe_0_0_0 = blocks.message_strobe(pmt.intern("em diferentes localidades "), 2000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("em diferentes tempos "), 2000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("o futuro ja chegou"), 2000)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_add_xx_0 = blocks.add_vcc(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.lora_sdr_add_crc_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.lora_sdr_header_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.lora_sdr_interleaver_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.lora_sdr_modulate_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.lora_sdr_whitening_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.lora_sdr_add_crc_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.lora_sdr_header_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.lora_sdr_interleaver_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.lora_sdr_modulate_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.lora_sdr_whitening_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.lora_sdr_add_crc_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.lora_sdr_header_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.lora_sdr_interleaver_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.lora_sdr_modulate_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.lora_sdr_whitening_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0_0, 'strobe'), (self.lora_sdr_add_crc_0_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0_0, 'strobe'), (self.lora_sdr_header_0_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0_0, 'strobe'), (self.lora_sdr_interleaver_0_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0_0, 'strobe'), (self.lora_sdr_modulate_0_0_0_0, 'msg'))
        self.msg_connect((self.blocks_message_strobe_0_0_0_0, 'strobe'), (self.lora_sdr_whitening_0_0_0_0, 'msg'))
        self.msg_connect((self.lora_sdr_crc_verif_0, 'msg'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.lora_sdr_frame_sync_0, 'new_frame'), (self.lora_sdr_deinterleaver_0, 'new_frame'))
        self.msg_connect((self.lora_sdr_frame_sync_0, 'new_frame'), (self.lora_sdr_dewhitening_0, 'new_frame'))
        self.msg_connect((self.lora_sdr_frame_sync_0, 'new_frame'), (self.lora_sdr_fft_demod_0, 'new_frame'))
        self.msg_connect((self.lora_sdr_frame_sync_0, 'new_frame'), (self.lora_sdr_hamming_dec_0, 'new_frame'))
        self.msg_connect((self.lora_sdr_frame_sync_0, 'new_frame'), (self.lora_sdr_header_decoder_0, 'new_frame'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CRC'), (self.lora_sdr_crc_verif_0, 'CRC'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'pay_len'), (self.lora_sdr_crc_verif_0, 'pay_len'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CR'), (self.lora_sdr_deinterleaver_0, 'CR'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'err'), (self.lora_sdr_dewhitening_0, 'CRC'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'pay_len'), (self.lora_sdr_dewhitening_0, 'pay_len'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CR'), (self.lora_sdr_fft_demod_0, 'CR'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CR'), (self.lora_sdr_frame_sync_0, 'CR'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CRC'), (self.lora_sdr_frame_sync_0, 'crc'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'err'), (self.lora_sdr_frame_sync_0, 'err'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'pay_len'), (self.lora_sdr_frame_sync_0, 'pay_len'))
        self.msg_connect((self.lora_sdr_header_decoder_0, 'CR'), (self.lora_sdr_hamming_dec_0, 'CR'))
        self.connect((self.blocks_add_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_throttle_1, 0), (self.lora_sdr_frame_sync_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.lora_sdr_add_crc_0, 0), (self.lora_sdr_hamming_enc_0, 0))
        self.connect((self.lora_sdr_add_crc_0_0, 0), (self.lora_sdr_hamming_enc_0_0, 0))
        self.connect((self.lora_sdr_add_crc_0_0_0, 0), (self.lora_sdr_hamming_enc_0_0_0, 0))
        self.connect((self.lora_sdr_add_crc_0_0_0_0, 0), (self.lora_sdr_hamming_enc_0_0_0_0, 0))
        self.connect((self.lora_sdr_deinterleaver_0, 0), (self.lora_sdr_hamming_dec_0, 0))
        self.connect((self.lora_sdr_dewhitening_0, 0), (self.lora_sdr_crc_verif_0, 0))
        self.connect((self.lora_sdr_fft_demod_0, 0), (self.lora_sdr_gray_enc_0, 0))
        self.connect((self.lora_sdr_frame_sync_0, 0), (self.lora_sdr_fft_demod_0, 0))
        self.connect((self.lora_sdr_gray_decode_0, 0), (self.lora_sdr_modulate_0, 0))
        self.connect((self.lora_sdr_gray_decode_0_0, 0), (self.lora_sdr_modulate_0_0, 0))
        self.connect((self.lora_sdr_gray_decode_0_0_0, 0), (self.lora_sdr_modulate_0_0_0, 0))
        self.connect((self.lora_sdr_gray_decode_0_0_0_0, 0), (self.lora_sdr_modulate_0_0_0_0, 0))
        self.connect((self.lora_sdr_gray_enc_0, 0), (self.lora_sdr_deinterleaver_0, 0))
        self.connect((self.lora_sdr_hamming_dec_0, 0), (self.lora_sdr_header_decoder_0, 0))
        self.connect((self.lora_sdr_hamming_enc_0, 0), (self.lora_sdr_interleaver_0, 0))
        self.connect((self.lora_sdr_hamming_enc_0_0, 0), (self.lora_sdr_interleaver_0_0, 0))
        self.connect((self.lora_sdr_hamming_enc_0_0_0, 0), (self.lora_sdr_interleaver_0_0_0, 0))
        self.connect((self.lora_sdr_hamming_enc_0_0_0_0, 0), (self.lora_sdr_interleaver_0_0_0_0, 0))
        self.connect((self.lora_sdr_header_0, 0), (self.lora_sdr_add_crc_0, 0))
        self.connect((self.lora_sdr_header_0_0, 0), (self.lora_sdr_add_crc_0_0, 0))
        self.connect((self.lora_sdr_header_0_0_0, 0), (self.lora_sdr_add_crc_0_0_0, 0))
        self.connect((self.lora_sdr_header_0_0_0_0, 0), (self.lora_sdr_add_crc_0_0_0_0, 0))
        self.connect((self.lora_sdr_header_decoder_0, 0), (self.lora_sdr_dewhitening_0, 0))
        self.connect((self.lora_sdr_interleaver_0, 0), (self.lora_sdr_gray_decode_0, 0))
        self.connect((self.lora_sdr_interleaver_0_0, 0), (self.lora_sdr_gray_decode_0_0, 0))
        self.connect((self.lora_sdr_interleaver_0_0_0, 0), (self.lora_sdr_gray_decode_0_0_0, 0))
        self.connect((self.lora_sdr_interleaver_0_0_0_0, 0), (self.lora_sdr_gray_decode_0_0_0_0, 0))
        self.connect((self.lora_sdr_modulate_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.lora_sdr_modulate_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.lora_sdr_modulate_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.lora_sdr_modulate_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.lora_sdr_whitening_0, 0), (self.lora_sdr_header_0, 0))
        self.connect((self.lora_sdr_whitening_0_0, 0), (self.lora_sdr_header_0_0, 0))
        self.connect((self.lora_sdr_whitening_0_0_0, 0), (self.lora_sdr_header_0_0_0, 0))
        self.connect((self.lora_sdr_whitening_0_0_0_0, 0), (self.lora_sdr_header_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sf_decode(self):
        return self.sf_decode

    def set_sf_decode(self, sf_decode):
        self.sf_decode = sf_decode
        self.set_frame_period((2^self.sf_decode)/self.bw)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_samp_rate(self.bw)
        self.set_frame_period((2^self.sf_decode)/self.bw)

    def get_sf_4(self):
        return self.sf_4

    def set_sf_4(self, sf_4):
        self.sf_4 = sf_4

    def get_sf_3(self):
        return self.sf_3

    def set_sf_3(self, sf_3):
        self.sf_3 = sf_3

    def get_sf_2(self):
        return self.sf_2

    def set_sf_2(self, sf_2):
        self.sf_2 = sf_2

    def get_sf_1(self):
        return self.sf_1

    def set_sf_1(self, sf_1):
        self.sf_1 = sf_1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_ruido(self):
        return self.ruido

    def set_ruido(self, ruido):
        self.ruido = ruido

    def get_pay_len(self):
        return self.pay_len

    def set_pay_len(self, pay_len):
        self.pay_len = pay_len

    def get_impl_head(self):
        return self.impl_head

    def set_impl_head(self, impl_head):
        self.impl_head = impl_head

    def get_has_crc(self):
        return self.has_crc

    def set_has_crc(self, has_crc):
        self.has_crc = has_crc

    def get_frame_period(self):
        return self.frame_period

    def set_frame_period(self, frame_period):
        self.frame_period = frame_period

    def get_cr(self):
        return self.cr

    def set_cr(self, cr):
        self.cr = cr


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
