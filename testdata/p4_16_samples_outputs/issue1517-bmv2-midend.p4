#include <core.p4>
#define V1MODEL_VERSION 20180101
#include <v1model.p4>

header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

struct meta_t {
}

struct headers_t {
    ethernet_t ethernet;
}

parser ParserImpl(packet_in packet, out headers_t hdr, inout meta_t meta, inout standard_metadata_t standard_metadata) {
    state start {
        packet.extract<ethernet_t>(hdr.ethernet);
        transition accept;
    }
}

control ingress(inout headers_t hdr, inout meta_t meta, inout standard_metadata_t standard_metadata) {
    @name("ingress.rand_int") bit<16> rand_int_0;
    @hidden action issue1517bmv2l62() {
        mark_to_drop(standard_metadata);
    }
    @hidden action issue1517bmv2l56() {
        random<bit<16>>(rand_int_0, 16w0, 16w49151);
    }
    @hidden table tbl_issue1517bmv2l56 {
        actions = {
            issue1517bmv2l56();
        }
        const default_action = issue1517bmv2l56();
    }
    @hidden table tbl_issue1517bmv2l62 {
        actions = {
            issue1517bmv2l62();
        }
        const default_action = issue1517bmv2l62();
    }
    apply {
        tbl_issue1517bmv2l56.apply();
        if (rand_int_0 < 16w32768) {
            tbl_issue1517bmv2l62.apply();
        }
    }
}

control egress(inout headers_t hdr, inout meta_t meta, inout standard_metadata_t standard_metadata) {
    apply {
    }
}

control DeparserImpl(packet_out packet, in headers_t hdr) {
    apply {
        packet.emit<ethernet_t>(hdr.ethernet);
    }
}

control verifyChecksum(inout headers_t hdr, inout meta_t meta) {
    apply {
    }
}

control computeChecksum(inout headers_t hdr, inout meta_t meta) {
    apply {
    }
}

V1Switch<headers_t, meta_t>(ParserImpl(), verifyChecksum(), ingress(), egress(), computeChecksum(), DeparserImpl()) main;