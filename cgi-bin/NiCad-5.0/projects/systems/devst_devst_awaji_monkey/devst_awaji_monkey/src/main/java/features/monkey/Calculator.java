public class Calculator {









































			public BigDecimal execute(Integer a, Integer b) {
				return BigDecimal.valueOf(a + b);
			};
		});


			public BigDecimal execute(Integer a, Integer b) {
				return BigDecimal.valueOf(a - b);
			};
		});


			public BigDecimal execute(Integer a, Integer b) {
				return BigDecimal.valueOf(a * b);
			};
		});


			public BigDecimal execute(Integer a, Integer b) {
				return BigDecimal.valueOf(a).divide(BigDecimal.valueOf(b), 3,
						BigDecimal.ROUND_HALF_UP);
			};
		});






	public String execute(String arg0) {
		String result = null;
		Matcher m = CALC_PATTERN.matcher(arg0);
		argumentCheck(m.matches(), "数式が正しくありません.[%s]", arg0);
		Integer a = Integer.valueOf(m.group(1));
		Integer b = Integer.valueOf(m.group(3));
		argumentCheck(a > 0, "左辺が正の整数ではありません.[%s]", arg0);
		argumentCheck(b > 0, "右辺が正の整数ではありません.[%s]", arg0);
		String operator = m.group(2);
		result = RESULT_FORMATTER.format(calculateExecuters.get(operator).execute(a, b));
		return result;
	}






































}
