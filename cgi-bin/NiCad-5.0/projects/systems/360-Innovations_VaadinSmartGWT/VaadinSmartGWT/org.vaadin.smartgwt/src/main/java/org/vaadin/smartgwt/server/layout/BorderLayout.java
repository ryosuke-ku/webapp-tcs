public class Borderlayout {

















































	public Canvas getCenterMember() {
		return center.getMembers().length > 0 ? center.getMembers()[0] : null;
	}

	public void setCenterMember(Canvas member) {
		if (member == null) {
			center.setWidth(0);
			center.setHeight(0);
			center.setMembers();
		} else {
			member.setHeight("100%");
			member.setWidth("100%");
			center.setWidth("100%");
			center.setMembers(member);
		}
	}

	public Canvas getNorthMember() {
		return north.getMembers().length > 0 ? north.getMembers()[0] : null;
	}

	public void setNorthMember(Canvas member) {
		if (member == null) {
			north.setHeight(0);
			north.setMembers();
		} else {
			member.setWidth("100%");
			north.setHeight(1);
			north.setMembers(member);
		}
	}

	public Canvas getSouthMember() {
		return south.getMembers().length > 0 ? south.getMembers()[0] : null;
	}

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

	public Canvas getWestMember() {
		return west.getMembers().length > 0 ? west.getMembers()[0] : null;
	}

	public void setWestMember(Canvas member) {
		if (member == null) {
			west.setWidth(0);
			west.setMembers();
		} else {
			member.setHeight("100%");
			west.setWidth(1);
			west.setMembers(member);
		}
	}

	public Canvas getEastMember() {
		return east.getMembers().length > 0 ? east.getMembers()[0] : null;
	}

	public void setEastMember(Canvas member) {
		if (member == null) {
			east.setWidth(0);
			east.setMembers();
		} else {
			member.setHeight("100%");
			east.setWidth(1);
			east.setMembers(member);
		}
	}
}
