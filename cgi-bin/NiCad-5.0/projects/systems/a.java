	public void setSouthMember(Canvas member) {
		if (member == null) {
			south.setHeight(0);
			south.setMembers();
		} else {
			member.setWidth("100%");
			south.setHeight(1);
			south.setMembers(member);
		}
	}