public class Myers {




	public String getName(int arg0, int arg1, int arg2) {
		// TODO Auto-generated method stub
		if (!isValidTriangle(arg0, arg1, arg2)) {
			throw new RuntimeException();
		}
		if ((arg0 == arg1) && (arg1 == arg2)) {
			return "正三角形";
		}
		if (arg0 == arg1) {
			return "二等辺三角形";
		}
		if (arg1 == arg2) {
			return "二等辺三角形";
		}
		if (arg0 == arg2) {
			return "二等辺三角形";
		}
		return "不等辺三角形";
	}


























}
