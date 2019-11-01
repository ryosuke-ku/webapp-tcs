	public HandlerRegistration addFormItemClickHandler(final FormItemClickHandler handler) {
		formItemClickHandlers.add(handler);
		return new HandlerRegistration() {
			@Override
			public void removeHandler() {
				formItemClickHandlers.remove(handler);
			}
		};
	}