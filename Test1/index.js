function pickUpSticks(n) {
	if(n<=0){
        return 0;
    }
    return pickUpSticks(n-3)+pickUpSticks(n-2)+pickUpSticks(n-1)+1;
}
console.log(pickUpSticks(2))