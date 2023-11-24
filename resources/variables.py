def get_variables(HOSTNAME):
    if HOSTNAME == "OLT4840E":
        USERNAME_PROMPT = "Username(1-32 chars):"
        PASSWORD_PROMPT = "Password(1-16 chars):"
    else:
        USERNAME_PROMPT = "Username(1-64 chars):"
        PASSWORD_PROMPT = "Password(1-96 chars):"

    return {
        "USR_PROMPT": HOSTNAME + ">",
        "EXC_PROMPT": HOSTNAME + "#",
        "CFG_PROMPT": HOSTNAME + "(config)#",
        "PROFILE_RULE_PROMPT": HOSTNAME + "(deploy-profile-rule)#",
        "PROFILE_LINE_PROMPT": HOSTNAME + "(deploy-profile-line)#",
        "PROFILE_DBA_PROMPT": HOSTNAME + "(deploy-profile-dba)#",
        "PROFILE_VLAN_PROMPT": HOSTNAME + "(deploy-profile-vlan)#",
        "PROFILE_UNIQUE_PROMPT": HOSTNAME + "(deploy-profile-unique)#",
        "PROFILE_ALARM_PROMPT": HOSTNAME + "(deploy-profile-alarm)#",
        "PROFILE_RULE1_PROMPT": HOSTNAME + "(deploy-profile-rule-0/1/1)#",
        "PROFILE_LINE1_PROMPT": HOSTNAME + "(deploy-profile-line-1)#",
        "PROFILE_DBA1_PROMPT": HOSTNAME + "(deploy-profile-dba-1)#",
        "PROFILE_VLAN1_PROMPT": HOSTNAME + "(deploy-profile-vlan-1)#",
        "PROFILE_UNIQUE1_PROMPT": HOSTNAME + "(deploy-profile-unique-0/1/1)#",
        "PROFILE_ALARM1_PROMPT": HOSTNAME + "(deploy-profile-alarm-1)#",
        "INTER_GPON1_PROMPT": HOSTNAME + "(config-if-gpon-0/1)#",
        "INTER_ETH1_PROMPT": HOSTNAME + "(config-if-ethernet-1/1)#",
        "INTER_PON1_PROMPT": HOSTNAME + "(config-if-pon-0/1)#",
        "INTER_VLAN1_PROMPT": HOSTNAME + "(config-if-vlanInterface-1)#",
        "PROFILE_WIFI1_PROMPT": HOSTNAME + "(deploy-profile-wifi-1)#",
        "USERNAME_PROMPT": USERNAME_PROMPT,
        "PASSWORD_PROMPT": PASSWORD_PROMPT,
        "ONU1_PROMPT": HOSTNAME + "(onu-0/1/1)#"

    }
