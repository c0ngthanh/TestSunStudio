class GameManager {
    private currentState: number[][]
    private magicTubes: number[]
    constructor(initState: number[][], magicTubes: number[]) {
        this.currentState = initState
        this.magicTubes = magicTubes
        //TODO: init instances of your classes and game logic here

        console.log('INIT GAME:')
        console.log(`Magic tubes indexes: ${magicTubes.join(', ')}`)
        this.printState()
    }

    public move(from: number, to: number): void {
        //TODO: call your methods of your instances to implement move function and update currentState here.
        let fromFlag = false;
        let toFlag = false;
        for (let i = 0; i < this.magicTubes.length; i++) {
            if(this.magicTubes[i]==from){
                fromFlag = true
            }
            if(this.magicTubes[i]==to){
                toFlag = true
            }
        }
        let temp = 100
        if(fromFlag){
            for(let index =0;index<this.currentState[from].length;index++){
                if (this.currentState[from][index] != 0){
                    temp = this.currentState[from][index]
                    this.currentState[from][index] =0
                    break;
                }
            }
        }else{
            for(let index =this.currentState[from].length-1;index>=0;index--){
                if (this.currentState[from][index] != 0){
                    temp = this.currentState[from][index]
                    this.currentState[from][index] =0
                    break;
                }
            }
        }
        // console.log(toFlag)
        if(toFlag){
            // this.currentState[to][0] =temp
            for(let index =this.currentState[to].length-1;index>=0;index--){
                if (this.currentState[to][index] == 0){
                    this.currentState[to][index] =temp
                    break;
                }
            }
        }else{
            for(let index =0;index<this.currentState[to].length;index++){
                // console.log(this.currentState[to][index])
                if (this.currentState[to][index] == 0){
                    this.currentState[to][index] = temp
                    break;
                }
            }
        }
        // if(this.magicTubes){

        // }
        // this.currentState[0][0] = 0; 


        console.log(`MOVE FROM ${from} TO ${to}:`)
        this.printState()

        if (this.isWin()) {
            console.log("YOU WIN")
        }
    }

    public isWin(): boolean {
        return this.currentState.every(tube => {
            const firstColor = tube[0]
            for (let i = 1; i < tube.length; i++) {
                const color = tube[i]

                if (firstColor != color) return false
            }

            return true
        })
    }

    private printState(): void {
        const transposing = this.currentState[0].map((_, colIndex) => this.currentState.map(row => row[row.length - 1 - colIndex]));

        console.log(transposing.map(row => row.join('\t')).join('\n'))
    }
}

export default GameManager