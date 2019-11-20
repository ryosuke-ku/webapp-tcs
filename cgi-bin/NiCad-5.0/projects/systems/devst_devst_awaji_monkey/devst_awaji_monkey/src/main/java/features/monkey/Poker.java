public class Poker {



















	public String poker(String... cards) {
		if (cards.length != NUMBER_OF_CARDS) {
			throw new RuntimeException();
		}

		Card[] hand = new Card[NUMBER_OF_CARDS];
		int i = 0;
		for (String card : cards) {
			hand[i] = cardFromString(card);
			i++;
		}
		Arrays.sort(hand);

		if (isDuplicate(hand)) {
			throw new RuntimeException();
		}

		boolean isFlush = isFlush(hand);
		boolean isStraight = isStraight(hand);
		boolean isRoyalStraight = isRoyalStraight(hand);

		if (isRoyalStraight && isFlush) {
			return "ロイヤルストレートフラッシュ";
		}

		if (isStraight && isFlush) {
			return "ストレートフラッシュ";
		}

		if (isFlush) {
			return "フラッシュ";
		}

		if (isStraight) {
			return "ストレート";
		}

		if (isFourOfAKind(hand)) {
			return "フォー・オブ・ア・カインド";
		}

		if (isFullHouse(hand)) {
			return "フルハウス";
		}

		if (isThreeOfAKind(hand)) {
			return "スリー・オブ・ア・カインド";
		}

		if (isTwoPair(hand)) {
			return "ツーペア";
		}

		if (isOnePair(hand)) {
			return "ワンペア";
		}

		return "ノーペア";
	}








































































































































































































































































		public boolean equals(Card other) {
			return this.getSuit().equals(other.getSuit())
					&& this.getLank().equals(other.getLank());
		}






















}
