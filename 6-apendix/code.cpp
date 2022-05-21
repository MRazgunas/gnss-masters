std::map<uint32_t, std::array<gr_complex, 4>> prn_phase_shifts = {
    { 2, std::array<gr_complex, 4>{ gr_complex(-0.7165653382097126, -0.6975199753959741), gr_complex(1.0, 0.0),gr_complex(-0.40497812574510855, 0.9143263737134454),gr_complex(-0.34756762205441344, -0.9376549195196708) } },
    { 5, std::array<gr_complex, 4>{ gr_complex(-0.8613362847130315, -0.5080352395619339), gr_complex(1.0, 0.0),gr_complex(-0.9078425843514135, -0.41931115181705664),gr_complex(0.9949826001738922, -0.10004811518065) } },
    { 9, std::array<gr_complex, 4>{ gr_complex(0.8775574285570917, 0.47947154199625314), gr_complex(1.0, 0.0),gr_complex(-0.850306890744293, -0.5262871759341785),gr_complex(-0.9985328523039517, -0.05414926472016588) } },
    { 16, std::array<gr_complex, 4>{ gr_complex(-0.762648410601778, 0.6468132665666203), gr_complex(1.0, 0.0),gr_complex(0.7858404188971819, 0.6184293298571),gr_complex(-0.19931165147309432, -0.9799361538320075) } },
    { 18, std::array<gr_complex, 4>{ gr_complex(0.8315945027152374, 0.5553832758139167), gr_complex(1.0, 0.0),gr_complex(-0.8377761846665095, 0.5460137950689768),gr_complex(-0.3934431395294178, 0.9193489522250162) } },
    { 20, std::array<gr_complex, 4>{ gr_complex(-0.6233198528674544, -0.7819669820531395), gr_complex(1.0, 0.0),gr_complex(-0.7314140387446979, 0.6819336506781063),gr_complex(-0.077344707765703, -0.9970044113145328) } },
    { 25, std::array<gr_complex, 4>{ gr_complex(0.19752959628155795, -0.9802969236883511), gr_complex(1.0, 0.0),gr_complex(0.6472121701396945, 0.7623099152071074),gr_complex(-0.6194465060984503, 0.7850388691538925) } },
    { 26, std::array<gr_complex, 4>{ gr_complex(-0.41037445758585406, 0.9119171039963644), gr_complex(1.0, 0.0),gr_complex(0.44821757272676555, 0.8939244976500681),gr_complex(0.6312479958002604, -0.7755810517271258) } },
    { 29, std::array<gr_complex, 4>{ gr_complex(0.6452068417239275, -0.7640079393518334), gr_complex(1.0, 0.0),gr_complex(0.5020534810787359, -0.8648365753925555),gr_complex(0.9846703507450776, -0.17442562989298863) } },
    { 31, std::array<gr_complex, 4>{ gr_complex(-0.6716897529989271, 0.7408325557885805), gr_complex(1.0, 0.0),gr_complex(-0.878634300963697, -0.47749530381987576),gr_complex(0.23642559028476792, 0.9716495974673685) } },
};

std::shared_ptr<gr_complex []> beam(new gr_complex[min_items]);

auto beam_prn = d_acquisition_gnss_synchro->PRN;

if (prn_phase_shifts.count(beam_prn) > 0) {
    auto s = prn_phase_shifts[beam_prn];
    for(int i = 0; i < min_items; i++) {
        beam.get()[i] = in[i]*s[0] + in1[i]*s[1] + in2[i]*s[2] + in3[i]*s[3];
    }
    in = beam.get();
}