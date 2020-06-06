def probability(pmb, pab, p1)
    return p1 * ((pmb * (1 - pab) + pab * (1 - pmb)))
end

def main
    pmb = gets.chomp.to_f
    pab = gets.chomp.to_f
    p1 = gets.chomp.to_f

    p = probability pmb, pab, p1

    puts "%.6f" % p
end

if __FILE__ == $0
    main
end
