# LoRa_GNURadio

## This is a LoRa implementation in GNU Radio 3.7

**This implementation was made by EPFL Telecommunication lab and it is available also here:**
**https://www.epfl.ch/labs/tcl/resources-and-sw/lora-phy/**


**FILES:**

Tx_Rx.grc
- A complete LoRa transmision, with no noise, no perpendicular signals.

Gaussian_Noise_Time_Demo.grc
- A demonstration of rms value of gaussian noise, sine wave rms value and the sum of them.

Tx_Rx_Perpendicular_sf.grc
- A transmission with sampling factor perpendicular signals

BER.grc
- A small demonstration of "Err measures" block on Bit Error Couting to make the proper bit error rate

Tx_Rx_gaussian_noise.grc
- A transmission with gaussian noise added to the channel.

Tx_Rx_transmission_amplitude.grc
- A transmission showing clear signal amplitude. 1,8pico pico as far as I can see.

Random_Message_Random_Delay.grc
- Generate random sequence of bytes at random intervals with random lenght.

	After some google, it is not random.
	https://www.gnuradio.org/doc/doxygen-3.2/pmt_8h-source.html
	https://www.gnuradio.org/doc/sphinx-3.7.0/pmt/boolean.html
	lines 00086 and 00087 shows that:
	extern const pmt_t PMT_T;       //< \#t : boolean true constant
	extern const pmt_t PMT_F;       //< \#f : boolean false constant 

Tx_RX_Char_seq.grc
- Transmission with char sequence
